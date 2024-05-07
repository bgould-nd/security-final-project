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
    if all (i < 256 for i in intList):
        return ''.join([chr(j) for j in intList])
    return ''.join(['\\' + hex(j)[1:] for j in intList])

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
def rsa_encrypt(plain, e, n, inputType='Binary'):
    
    intList = plain

    if inputType == 'Text':
        intList = string2intlist(plain)
    if inputType == 'File':
        intList = binary2intList(image2binary(plain))
    if inputType == 'Binary':
        intList = binary2intList(plain)
    if inputType == 'Hex':
        intList = hex2intList(plain)

    encrypted = [pow(num, e, n) for num in intList]

    if inputType == 'Text':
        return intList2hex(encrypted)
    if inputType == 'File':
        binary2image(intList2binary(encrypted), 'output.bin')
        return
    if inputType == 'Binary':
        return intList2binary(encrypted)
    if inputType == 'Hex':
        return intList2hex(encrypted)
    return encrypted
    
#Decrypting function using public key (e,n) and private key d and encrypted text encrypted. Encrypted is an array of numbers, each number represents a character in the encrypted message, returns an array of decrypted message.
def rsa_decrypt(encrypted, d, n, inputType='Binary'):
    
    intList = encrypted

    if inputType == 'Text':
        intList = string2intlist(encrypted)
    if inputType == 'File':
        intList = binary2intList(image2binary(encrypted))
    if inputType == 'Binary':
        intList = binary2intList(encrypted)
    if inputType == 'Hex':
        intList = hex2intList(encrypted)

    decrypted = [pow(num, d, n) for num in intList]
    
    if inputType == 'Text' or inputType == 'Hex':
        return intList2hex(decrypted)
    if inputType == 'File':
        return binary2image(intList2binary(intList), 'output.bin')
    if inputType == 'Binary':
        return intList2binary(decrypted)
    return decrypted

def test():
    e, d, n = 3, 2799531, 4203469
    print(rsa_decrypt(rsa_encrypt('hello world', e, n, 'ascii'), d, n, 'hex'))
