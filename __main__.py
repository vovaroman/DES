from DES import DES

des = DES()
encrypted = des.process(input('input text: '),input('input pass: '),True)
print(encrypted)

decrypted = des.process(encrypted,input('input pass:'), False)
print(decrypted)
