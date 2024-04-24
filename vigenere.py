'''
Vigenere cipher backend
'''

import string

def char2num(c):
    '''Convert a letter to its index in the English alphabet from 0-25'''
    return ord(c.lower()) - ord('a')

def key2shift(key):
    '''Convert a string of text to a list of integer shift values'''
    return [char2num(c) for c in key.replace(' ', '')]

def shiftChar(c, shift):
    '''Shift a single character by the given integer'''
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return c.translate(table)

def shiftString(text, shiftList):
    '''Handle non-alphanumeric characters with key alignment'''
    i = 0
    shifted = ''
    for c in text:
        if c.isalpha():
            shifted += shiftChar(c, shiftList[i])
            i += 1
        else:
            shifted += c
    return shifted

def keyLength(key, l):
    '''Copy the key to fill the length of plain/ciphertext'''
    key *= int(l/len(key)) + 1
    return key[:l]

def clean(key, text):
    '''Convert to lowercase and set appropriate key length'''
    key = keyLength(key.lower(), len(text))
    text = text.lower()
    return key, text

def vin_encrypt(key, plaintext):
    key, plaintext = clean(key, plaintext)
    return shiftString(plaintext, key2shift(key))

def vin_decrypt(key, ciphertext):
    key, ciphertext = clean(key, ciphertext)
    reverseShift = [26 - i for i in key2shift(key)]
    return shiftString(ciphertext, reverseShift)

if __name__ == '__main__':
    print(vin_encrypt('test', 'The quick brown fox jumps over the lazy dog.'))
    print(vin_decrypt('test', vin_encrypt('test', 'The quick brown fox jumps over the lazy dog.')))