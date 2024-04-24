# Handle file types (text, binary, image)
# Chunk input strings for plaintext
# Pad input (keys chopped to length, and plaintext)
# Input type as parameter

def string2intlist(string):
    return [ord(c.lower()) - ord('a') + 1 for c in string]

def intList2string(intList):
    return ''.join([chr(i - 1 + ord('a')) for i in intList])

#Encrypting function using public key (e,n) and private key d, and plaintext plain, plain is received as an array of numbers, each number represents a character in the plaintext message, returns an array
def rsa_encrypt(plain, e, n):
    encrypted = []
    for num in plain: 
        encrypted.append(pow(num, e)%n)

    return(encrypted)
#Decrypting function using public key (e,n) and private key d and encrypted text encrypted. Encrypted is an array of numbers, each number represents a character in the encrypted message, returns an array of decrypted message.
def rsa_decrypt(encrypted, d, n):
    decrypted = []
    for num in encrypted:
        decrypted.append(pow(num, d)%n)
    return(decrypted)
