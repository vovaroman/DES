
from Matrix import Matrix
from PIMatrix import PIMatrix
from Helper import Helper
from KeyMatrix import KeyMatrix
from KeyMatrixfin import KeyMatrixfin
from EMatrix import EMatrix
from SBox import SBox
from PBox import PBox
from PIBox import PIBox

class DES:

    '''
    При старте алгоритма создаем все вспомогательные таблицы
    '''
    def __init__(self):
        self.PI = PIMatrix()
        self.E = EMatrix()
        self.KeyMatrix = KeyMatrix()
        self.KeyMatrixfin = KeyMatrixfin()
        self.helper = Helper()
        self.SBox = SBox().value
        self.PBox = PBox().value
        self.PIBox = PIBox().value
        self.steps = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
        self.keys = None
    


    '''
     Метод process шифрует и дешифрует данные.

     args:
        text - текст для шифрования
        password - пароль шифрования
        encrypt - True (шифрует) / False (расшифрует)
    '''
    def process(self, text, password, encrypt = True):
        self.text = text
        if len(password) < 8:
            print(f'password length should be more than 8, now it is - {len(password)}')
            return
        elif len(password) > 8:
            password = password[:8]
            print(f'password was cutted to be 8 bytes. password - {password}')
        self.password = password
        #добавляем символы для того чтоб размер текста был % 8 == 0
        padding = False
        if len(self.text) % 8 != 0:
            padding = True

        if padding:
            pad_len = 8 - (len(self.text) % 8)
            self.text += pad_len * chr(pad_len)
        self.generateKeys()
        blocks = self.helper.nsplit(self.text,8)
        result = list()
        for block in blocks:
            block = self.helper.getBitArrayFromString(block)
            block = self.helper.permut(block, self.PI.value)
            g, d = self.helper.nsplitMatrixInList(block, 32)
            tmp = None
            for i in range(16):
                d_e = self.helper.permut(d, self.E.value)
                d_e = [item for x in d_e for item in x]
                if encrypt == True:
                    tmp = self.helper.xor(self.keys[i], d_e)
                else:
                    tmp = self.helper.xor(self.keys[15-i], d_e)#If decrypt start by
                tmp = self.processSBox(tmp) #Method that will apply the SBOXes
                tmp = self.helper.permutDefault(tmp, self.PBox)
                tmp = self.helper.xor(g, tmp)
                g = d
                d = tmp
            result += self.helper.permutDefault(d+g, self.PIBox)
        final_res = self.helper.getStringFromBitArray(result)
        if padding and encrypt == False:
            final_res = self.helper.removePadding(final_res) 
        return final_res

    '''
        Обрабатываем входные данные и производим shuffle используя SBox

        S-блок - «блок подстановок»
    '''
    def processSBox(self, d_e):
        subblocks = self.helper.nsplit(d_e, 6)
        result = list()
        for i in range(len(subblocks)):
            block = subblocks[i]
            row = int(str(block[0])+str(block[5]),2)
            column = int(''.join([str(x) for x in block[1:][:-1]]),2) 
            val = self.SBox[i][row][column] 
            bin = self.helper.binvalue(val, 4)
            result += [int(x) for x in bin]
        return result

    def generateKeys(self):
        self.keys = []
        key = self.helper.getBitArrayFromString(self.password)
        key = self.helper.permut(key, self.KeyMatrix.value) 
        g, d = self.helper.nsplitMatrixInList(key, 28)
        for i in range(16):
            g, d = self.helper.shift(g, d, self.steps[i]) 
            tmp = g + d 
            permutData = self.helper.permut(tmp, self.KeyMatrixfin.value)
            permutData = [y for x in permutData for y in x]
            self.keys.append(permutData) 

'''
   Функция которая заготавливает ключи для шифрования прогоняя данные в 16 раундах
'''