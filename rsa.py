'''
RSA backend
'''

def string2intlist(string):
    return [ord(c) for c in string]

def intList2string(intList):
    return ''.join([chr(i) for i in intList])

def hex2intList(hex):
    return [int(i, 16) for i in hex.split('\\x')[1:]]

def intList2hex(intList):
    return ''.join(['\\' + hex(i)[1:] for i in intList])

def binary2intList(bin):
    return [int(bin[i:i+8],2) for i in range(0,len(bin),8)]

def intList2binary(intList):
    return ''.join(format(i, '08b') for i in intList)

def image2binary(filename):
    with open(filename, 'rb') as fd:
        return ''.join([format(x, 'b') for x in fd.read()])
    
def binary2image(bin, filename):
    with open(filename, 'wb') as fd:
        fd.write(bytearray(bin, 'ascii'))
    return

#Encrypting function using public key (e,n) and private key d, and plaintext plain, plain is received as an array of numbers, each number represents a character in the plaintext message, returns an array
def rsa_encrypt(plain, e, n, inputType='binary'):
    
    intList = plain

    if inputType == 'ascii':
        intList = string2intlist(plain)
    if inputType == 'image':
        intList = binary2intList(image2binary(plain))
    if inputType == 'binary':
        intList = binary2intList(plain)
    if inputType == 'hex':
        intList = hex2intList(plain)

    encrypted = [pow(num, e, n) for num in intList]

    if inputType == 'ascii':
        return intList2hex(encrypted)
    if inputType == 'image':
        intList = binary2intList(image2binary(encrypted))
    if inputType == 'binary':
        intList = binary2intList(encrypted)
    if inputType == 'hex':
        intList = intList2hex(encrypted)
    return encrypted
    
#Decrypting function using public key (e,n) and private key d and encrypted text encrypted. Encrypted is an array of numbers, each number represents a character in the encrypted message, returns an array of decrypted message.
def rsa_decrypt(encrypted, d, n, inputType='binary'):
    
    intList = encrypted

    if inputType == 'ascii':
        intList = string2intlist(encrypted)
    if inputType == 'image':
        intList = binary2intList(image2binary(encrypted))
    if inputType == 'binary':
        intList = binary2intList(encrypted)
    if inputType == 'hex':
        intList = hex2intList(encrypted)

    decrypted = [pow(num, d, n) for num in intList]
    
    if inputType == 'ascii' or 'hex':
        return intList2string(decrypted)
    if inputType == 'image':
        return binary2image(intList2binary(intList), 'output.bin')
    if inputType == 'binary':
        return intList2binary(decrypted)
    return decrypted

def test():
    e, d, n = 3, 2799531, 4203469
    print(rsa_decrypt(rsa_encrypt('hello world', e, n, 'ascii'), d, n, 'hex'))
