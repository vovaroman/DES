
def nsplit(s, n):
    return [s[k:k+n] for k in range(0, len(s), n)]


def getStringFromBitArray(array):
    res = ''.join([chr(int(y,2)) for y in [''.join([str(x) for x in _bytes]) for _bytes in  nsplit(array,8)]])
    return res

def getBitArrayFromString(text):
    output = list()
    for char in text:
        binval = binvalue(char, 8)
        output.extend([int(x) for x in list(binval)])
    return output

def binvalue(val, bitsize): 
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = f'0{binval}'
    # print('final binval',binval)
    return binval

#i = nsplit([0,1,1,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,1,1,1,0,1,1,0,1,0,0,0,0,1,1,1,0,0,0,0],8)

#a = getStringFromBitArray([0,1,1,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,1,1,1,0,1,1,0,1,0,0,0,0,1,1,1,0,0,0,0])

#print(a)