# Handle file types (text, binary, image)
# Chunk input strings for plaintext
# Input type as parameter

def string2intlist(string):
    l = [ord(c) for c in string]
    print(l)
    return l

def intList2string(intList):
    l = ''.join([chr(i) for i in intList])
    print(intList)
    return l

def binary2intList(bin):
    return [int(bin[i:i+8],2) for i in range(0,len(bin),8)]

def intList2binary(intList):
    return ''.join(format(i, '08b') for i in intList)

def image2binary(filename):
    with open(filename, 'rb') as fd:
        return ''.join([format(x, 'b') for x in fd.read()])

#Encrypting function using public key (e,n) and private key d, and plaintext plain, plain is received as an array of numbers, each number represents a character in the plaintext message, returns an array
def rsa_encrypt(plain, e, n, inputType='binary'):
    
    intList = plain

    if inputType == 'ascii':
        intList = string2intlist(plain)
    if inputType == 'image':
        intList = binary2intList(image2binary(plain))
    if inputType == 'binary':
        intList = binary2intList(plain)

    encrypted = []
    for num in intList: 
        encrypted.append(pow(num, e)%n)

    if inputType == 'ascii':
        return intList2string(encrypted)
    if inputType == 'image' or inputType == 'binary':
        return intList2binary(encrypted)
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

    decrypted = []
    for num in intList:
        decrypted.append(pow(num, d)%n)
    
    if inputType == 'ascii':
        return intList2string(decrypted)
    if inputType == 'image' or inputType == 'binary':
        return intList2binary(decrypted)
    return decrypted

#17, 53, 77
print(rsa_encrypt([4], 17, 77, 'int'))
print(rsa_decrypt(rsa_encrypt([4], 17, 77, 'int'), 53, 77, 'int'))

print(rsa_encrypt('hello world', 17, 77, 'ascii'))
print(rsa_decrypt(rsa_encrypt('hello world', 17, 77, 'ascii'), 53, 77, 'ascii'))
print(len(rsa_decrypt(rsa_encrypt('hello world', 17, 77, 'ascii'), 53, 77, 'ascii')))

print(rsa_encrypt('mario.jpg', 163, 969, 'image')[:64])
