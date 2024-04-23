'''
Triple DES backend
'''

def arr2binInt(a):
    a = [str(i) for i in a]
    return int(''.join(a), 2)

def int2bytes(i: int) -> bytes:
    return i.to_bytes(((i.bit_length() + 7) // 8), byteorder='big')

def xor(a, b):
    return [int(a1) ^ int(b1) for a1, b1 in zip(a, b)]

def string2binary(text):
    return ''.join(format(ord(i), '08b') for i in text)

def binary2string(bin):
    return "".join([chr(int(bin[i:i+8],2)) for i in range(0,len(bin),8)])

def splitString(text, size=64):
    text = [text[i:i+size] for i in range(0, len(text), size)]
    if len(text[-1]) < size:
        text[-1] += '0'*(size-len(text[-1]))
    return text

def generateKeys(key):

    pc1 = [57, 49, 41, 33, 25, 17, 9,
           1,  58, 50, 42, 34, 26, 18,
           10, 2,  59, 51, 43, 35, 27,
           19, 11, 3,  60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7,  62, 54, 46, 38, 30, 22,
           14, 6,  61, 53, 45, 37, 29,
           21, 13, 5,  28, 20, 12, 4]
    
    key = [key[i-1] for i in pc1]
    c0, d0 = key[:28], key[28:]

    leftShifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    combined = []

    pc2 = [14, 17, 11, 24, 1,  5,
           3,  28, 15, 6,  21, 10,
           23, 19, 12, 4,  26, 8,
           16, 7,  27, 20, 13, 2,
           41, 52, 31, 37, 47, 55,
           30, 40, 51, 45, 33, 48,
           44, 49, 39, 56, 34, 53,
           46, 42, 50, 36, 29, 32]

    keys = []
    for i in range(16):
        c0 = c0[leftShifts[i]:] + c0[:leftShifts[i]]
        d0 = d0[leftShifts[i]:] + d0[:leftShifts[i]]
        combined = c0 + d0
        keys.append([combined[i-1] for i in pc2])

    return keys

def encode(key, plaintext):

    keys = generateKeys(key)
    
    ip = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]
    
    message = [plaintext[i-1] for i in ip]
    l0, r0 = message[:32], message[32:]

    expansion = [32, 1,  2,  3,  4,  5,
                 4,  5,  6,  7,  8,  9,
                 8,  9,  10, 11, 12, 13,
                 12, 13, 14, 15, 16, 17,
                 16, 17, 18, 19, 20, 21,
                 20, 21, 22, 23, 24, 25,
                 24, 25, 26, 27, 28, 29,
                 28, 29, 30, 31, 32, 1]

    ln_1, rn_1 = None, None
    for i in range(16):
        ln_1 = r0
        rExp = [r0[j-1] for j in expansion]
        rXor = xor(rExp, keys[i])
        start, end = 0, 6
        sInput = []
        for _ in range(8):
            sInput.append(rXor[start:end])
            start += 6
            end += 6
        rn_1 = f(sInput, l0)
        r0 = rn_1
        l0 = ln_1

        ipInv = [40, 8, 48, 16, 56, 24, 64, 32,
             39, 7, 47, 15, 55, 23, 63, 31,
             38, 6, 46, 14, 54, 22, 62, 30,
             37, 5, 45, 13, 53, 21, 61, 29,
             36, 4, 44, 12, 52, 20, 60, 28,
             35, 3, 43, 11, 51, 19, 59, 27,
             34, 2, 42, 10, 50, 18, 58, 26,
             33, 1, 41, 9,  49, 17, 57, 25]

    rl = r0 + l0
    rlP = [rl[i-1] for i in ipInv]

    return ''.join([str(i) for i in rlP])

def decode(key, ciphertext):

    keys = generateKeys(key)

    ip = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]
    
    message = [ciphertext[i-1] for i in ip]
    l0, r0 = message[:32], message[32:]

    expansion = [32, 1,  2,  3,  4,  5,
                 4,  5,  6,  7,  8,  9,
                 8,  9,  10, 11, 12, 13,
                 12, 13, 14, 15, 16, 17,
                 16, 17, 18, 19, 20, 21,
                 20, 21, 22, 23, 24, 25,
                 24, 25, 26, 27, 28, 29,
                 28, 29, 30, 31, 32, 1]

    ln_1, rn_1 = None, None
    for i in range(15, -1, -1):
        ln_1 = r0
        rExp = [r0[j-1] for j in expansion]
        rXor = xor(rExp, keys[i])
        start, end = 0, 6
        sInput = []
        for _ in range(8):
            sInput.append(rXor[start:end])
            start += 6
            end += 6
        rn_1 = f(sInput, l0)
        r0 = rn_1
        l0 = ln_1
    
    ipInv = [40, 8, 48, 16, 56, 24, 64, 32,
             39, 7, 47, 15, 55, 23, 63, 31,
             38, 6, 46, 14, 54, 22, 62, 30,
             37, 5, 45, 13, 53, 21, 61, 29,
             36, 4, 44, 12, 52, 20, 60, 28,
             35, 3, 43, 11, 51, 19, 59, 27,
             34, 2, 42, 10, 50, 18, 58, 26,
             33, 1, 41, 9,  49, 17, 57, 25]

    rl = r0 + l0
    rlP = [rl[i-1] for i in ipInv]
    return ''.join([str(i) for i in rlP])

def f(input, l):

    sBoxes = [
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ],
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
        ],
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ],
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ],
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ],
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ]
    ]

    sOutput = ''
    for i in range(8):
        temp = input[i]
        row = (temp[0] << 1) + temp[5]
        col = (temp[1] << 3) + (temp[2] << 2) + (temp[3] << 1) + temp[4]
        sVal = sBoxes[i][row][col]
        sOutput += f'{sVal:04b}'
    
    p = [16, 7,  20, 21,
         29, 12, 28, 17,
         1,  15, 23, 26,
         5,  18, 31, 10,
         2,  8,  24, 14,
         32, 27, 3,  9,
         19, 13, 30, 6,
         22, 11, 4,  25]

    sP = [sOutput[i-1] for i in p]
    output = xor(sP, l)
    return output

def tripleEncode(k1, k2, k3, plaintext, inputType='binary'):

    binary = plaintext

    if inputType == 'ascii':
        binary = string2binary(plaintext)

    if len(binary) > 64:
        binary = splitString(binary)
    else:
        binary = [binary]

    encodedBinary = ''
    for b in binary:
        curr = encode(k3, decode(k2, encode(k1, b)))
        encodedBinary += curr

    if inputType == 'ascii':
        return binary2string(encodedBinary)
    
    return encodedBinary

def tripleDecode(k1, k2, k3, ciphertext, inputType='binary'):

    binary = ciphertext
    
    if inputType == 'ascii':
        binary = string2binary(ciphertext)

    if len(binary) > 64:
        binary = splitString(binary)
    else:
        binary = [binary]
    
    decodedBinary = ''
    for b in binary:
        curr = decode(k1, encode(k2, decode(k3, b)))
        decodedBinary += curr

    if inputType == 'ascii':
        return binary2string(decodedBinary)
    
    return decodedBinary

if __name__ == '__main__':

    k1       = '0100110001001111010101100100010101000011010100110100111001000100'
    k2       = '0100110001001111010101100100010101000011010100110100111001000111'
    k3       = '1000110001001111010101100100010101000011010100110100111001000100'

    plaintext = '11001010111011011010001001100101010111111011011100111000011100111111'

    ascii_plaintext = 'hello world'

    encoded = tripleEncode(k1, k2, k3, plaintext, inputType='binary')
    decoded = tripleDecode(k1, k2, k3, encoded, inputType='binary')
    print(decoded)
    print(plaintext)

    ascii_encoded = tripleEncode(k1, k2, k3, ascii_plaintext, inputType='ascii')
    ascii_decoded = tripleDecode(k1, k2, k3, ascii_encoded, inputType='ascii')
    print(ascii_decoded)
    print(ascii_plaintext)
