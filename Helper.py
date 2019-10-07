class Helper:
    def __init__(self):
        pass
    def getBitArrayFromString(self, text):
        output = list()
        for char in text:
            binval = self.binvalue(char, 8)
            output.extend([int(x) for x in list(binval)])
        return output

    def getStringFromBitArray(self, array): #Recreate the string from the bit array
        res = ''.join([chr(int(y,2)) for y in [''.join([str(x) for x in _bytes]) for _bytes in  self.nsplit(array,8)]])   
        return res

    def binvalue(self, val, bitsize): 
        binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
        if len(binval) > bitsize:
            raise "binary value larger than the expected size"
        while len(binval) < bitsize:
            binval = f'0{binval}'
        # print('final binval',binval)
        return binval

    def nsplitMatrixInList(self,s,n):
        l =  list();
        for x in s:
            for y in x:
                l.append(y)
        return self.nsplit(l,n)

    def nsplit(self, s, n):#Split a list into sublists of size "n"
        return [s[k:k+n] for k in range(0, len(s), n)]
    def permutDefault(self, block, table):#Permut the given block using the given table (so generic method)
        return [block[x-1] for x in table]
    def permut(self, block, table):#Permut the given block using the given table (so generic method)
        output = list()
        for x in table:
            ylist = list()
            for y in x:
                ylist.append(block[y-1])
            output.append(ylist)
        return output
    def xor(self, t1, t2): #xor
        return [x^y for x,y in zip(t1,t2)]
    
    def removePadding(self, data):#Remove the padding of the plain text (it assume there is padding)
        pad_len = ord(data[-1])
        return data[:-pad_len]
    def shift(self, g, d, n): #Shift a list of the given value
        return g[n:] + g[:n], d[n:] + d[:n]