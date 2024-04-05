import os



#Encrypting function using public key (e,n) and private key d, and plaintext plain, plain is received as an array of numbers, each number represents a character in the plaintext message, returns an array

def encrypt(plain, e, n):
    encrypted = []
    for num in plain: 
        encrypted.append((num**e)%n)

    return(encrypted)
#Decrypting function using public key (e,n) and private key d and encrypted text encrypted. Encrypted is an array of numbers, each number represents a character in the encrypted message, returns an array of decrypted message.
def decrypt(encrypted, d, n):
    decrypted = []
    for num in encrypted:
        decrypted.append((num**d)%n)
    return(decrypted)
#Test functionality
plainText = [7,4,11,11,14]

print(encrypt(plainText,17,77))
message = [28,16,44,44,42]

print(decrypt(message,53,77))



