import time

from TripleDes import tripleEncode, tripleDecode
from vigenere import vin_encrypt, vin_decrypt
from rsa import rsa_decrypt, rsa_encrypt
from aesDecrypt import aes_decrypt
from aesEncrypt import aes_encrypt

aes_key = "00101011011111100001010100010110001010001010111011010010101001101010101111110111000101011000100000001001110011110100111100111100"

k1       = '0100110001001111010101100100010101000011010100110100111001000100'
k2       = '0100110001001111010101100100010101000011010100110100111001000111'
k3       = '1000110001001111010101100100010101000011010100110100111001000100'

e, d, n = 3, 2799531, 4203469

vin_key = 'test'*100

binary1 =  '11001010111011011010001001100101010111111011011100111000011100111111'*10
binary2 = '110010101110110110100010011001010101111110110111001110000111001111111'*1000

text1 = 'The quick brown fox jumps over the lazy dog.'*10
text2 = 'The quick brown fox jumps over the lazy dog.'*1000

image1 = '../image1.jpg' #file size 62,000 bytes
image2 = '../image2.jpg' #file size 5,800 bytes

start_time = time.time()
result = tripleEncode(k1, k2, k3, image1, inputType='File')
end_time = time.time()
print(f"Running 3DES encrypt on input type file1 (66,000 bytes) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = tripleEncode(k1, k2, k3, image2, inputType='File')
end_time = time.time()
print(f"Running 3DES encrypt on input type file2 (5,800 bytes) took {end_time - start_time:.6f} seconds")
    
start_time = time.time()
result = tripleEncode(k1, k2, k3, binary1, inputType='Binary')
end_time = time.time()
print(f"Running 3DES encrypt on input type binary1 (64 bit) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = tripleEncode(k1, k2, k3, binary2, inputType='Binary')
end_time = time.time()
print(f"Running 3DES encrypt on input type binary1 (128 bit) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = tripleEncode(k1, k2, k3, text1, inputType='Text')
end_time = time.time()
print(f"Running 3DES encrypt on input type text1 (length: 44) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = tripleEncode(k1, k2, k3, text2, inputType='Text')
end_time = time.time()
print(f"Running 3DES encrypt on input type text2 (length: 88) took {end_time - start_time:.6f} seconds")

print()

start_time = time.time()
result = tripleDecode(k1, k2, k3, image1, inputType='File')
end_time = time.time()
print(f"Running 3DES decrypt on input type file1 (66,000 bytes) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = tripleDecode(k1, k2, k3, image2, inputType='File')
end_time = time.time()
print(f"Running 3DES decrypt on input type file2 (5,800 bytes) took {end_time - start_time:.6f} seconds")
    
start_time = time.time()
result = tripleDecode(k1, k2, k3, binary1, inputType='Binary')
end_time = time.time()
print(f"Running 3DES decrypt on input type binary1 (64 bit) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = tripleDecode(k1, k2, k3, binary2, inputType='Binary')
end_time = time.time()
print(f"Running 3DES decrypt on input type binary1 (128 bit) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = tripleDecode(k1, k2, k3, text1, inputType='Text')
end_time = time.time()
print(f"Running 3DES decrypt on input type text1 (length: 44) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = tripleDecode(k1, k2, k3, text2, inputType='Text')
end_time = time.time()
print(f"Running 3DES decrypt on input type text2 (length: 88) took {end_time - start_time:.6f} seconds")

print()

start_time = time.time()
result = aes_encrypt(aes_key, image1, inputType='File')
end_time = time.time()
print(f"Running aes encrypt on input type file1 (66,000 bytes) took {end_time - start_time:.6f} seconds")
start_time = time.time()
result = aes_encrypt(aes_key, image2, inputType='File')
end_time = time.time()
print(f"Running aes encrypt on input type file2 (5,800 bytes) took {end_time - start_time:.6f} seconds")
    
start_time = time.time()
result = aes_encrypt(aes_key, binary1, inputType='Binary')
end_time = time.time()
print(f"Running aes encrypt on input type binary1 (64 bit) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = aes_encrypt(aes_key, binary2, inputType='Binary')
end_time = time.time()
print(f"Running aes encrypt on input type binary1 (128 bit) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = aes_encrypt(aes_key, text1, inputType='Text')
end_time = time.time()
print(f"Running aes encrypt on input type text1 (length: 44) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = aes_encrypt(aes_key, text2, inputType='Text')
end_time = time.time()
print(f"Running aes encrypt on input type text2 (length: 88) took {end_time - start_time:.6f} seconds")

print()

start_time = time.time()
result = aes_decrypt(aes_key, image1, inputType='File')
end_time = time.time()
print(f"Running aes decrypt on input type file1 (66,000 bytes) took {end_time - start_time:.6f} seconds")
start_time = time.time()
result = aes_decrypt(aes_key, image2, inputType='File')
end_time = time.time()
print(f"Running aes decrypt on input type file2 (5,800 bytes) took {end_time - start_time:.6f} seconds")
    
start_time = time.time()
result = aes_decrypt(aes_key, binary1, inputType='Binary')
end_time = time.time()
print(f"Running aes decrypt on input type binary1 (64 bit) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = aes_decrypt(aes_key, binary2, inputType='Binary')
end_time = time.time()
print(f"Running aes decrypt on input type binary1 (128 bit) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = aes_decrypt(aes_key, text1, inputType='Text')
end_time = time.time()
print(f"Running aes decrypt on input type text1 (length: 44) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = aes_decrypt(aes_key, text2, inputType='Text')
end_time = time.time()
print(f"Running aes decrypt on input type text2 (length: 88) took {end_time - start_time:.6f} seconds")

print()

start_time = time.time()
result = rsa_encrypt(image1, e, n, inputType='File')
end_time = time.time()
print(f"Running RSA encrypt on input type file1 (66,000 bytes) took {end_time - start_time:.6f} seconds")
start_time = time.time()
result = rsa_encrypt(image2, e, n,inputType='File')
end_time = time.time()
print(f"Running RSA encrypt on input type file2 (5,800 bytes) took {end_time - start_time:.6f} seconds")
   
start_time = time.time()
result = rsa_encrypt(binary1, e, n,inputType='Binary')
end_time = time.time()
print(f"Running RSA encrypt on input type binary1 (64 bit) took {end_time - start_time:.6f} seconds")
start_time = time.time()
result = rsa_encrypt(binary2, e, n,inputType='Binary')
end_time = time.time()
print(f"Running RSA encrypt on input type binary1 (128 bit) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = rsa_encrypt(text1, e, n,inputType='Text')
end_time = time.time()
print(f"Running RSA encrypt on input type text1 (length: 44) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = rsa_encrypt(text2, e, n,inputType='Text')
end_time = time.time()
print(f"Running RSA encrypt on input type text2 (length: 88) took {end_time - start_time:.6f} seconds")

print()

start_time = time.time()
result = rsa_decrypt(image1, d, n, inputType='File')
end_time = time.time()
print(f"Running RSA decrypt on input type file1 (66,000 bytes) took {end_time - start_time:.6f} seconds")
start_time = time.time()
result = rsa_decrypt(image2, d, n,inputType='File')
end_time = time.time()
print(f"Running RSA decrypt on input type file2 (5,800 bytes) took {end_time - start_time:.6f} seconds")
   
start_time = time.time()
result = rsa_decrypt(binary1, d, n,inputType='Binary')
end_time = time.time()
print(f"Running RSA decrypt on input type binary1 (64 bit) took {end_time - start_time:.6f} seconds")
start_time = time.time()
result = rsa_decrypt(binary2, d, n,inputType='Binary')
end_time = time.time()
print(f"Running RSA decrypt on input type binary1 (128 bit) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = rsa_decrypt(text1, d, n, inputType='Text')
end_time = time.time()
print(f"Running RSA decrypt on input type text1 (length: 44) took {end_time - start_time:.6f} seconds")
start_time = time.time()
result = rsa_decrypt(text2, d, n, inputType='Text')
end_time = time.time()
print(f"Running RSA decrypt on input type text2 (length: 88) took {end_time - start_time:.6f} seconds")

print()

start_time = time.time()
result = vin_encrypt(vin_key, text1)
end_time = time.time()
print(f"Running Vigenere encrypt on input type text2 (length: 88) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = vin_encrypt(vin_key, text2)
end_time = time.time()
print(f"Running Vigenere encrypt on input type text2 (length: 88) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = vin_decrypt(vin_key, text1)
end_time = time.time()
print(f"Running Vigenere decrypt on input type text2 (length: 88) took {end_time - start_time:.6f} seconds")

start_time = time.time()
result = vin_decrypt(vin_key, text2)
end_time = time.time()
print(f"Running Vigenere decrypt on input type text2 (length: 88) took {end_time - start_time:.6f} seconds")