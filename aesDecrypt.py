import os
import numpy as np 
S_BOX =  [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
		0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
		0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
		0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
		0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
		0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
		0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
		0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
		0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
		0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
		0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
		0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
		0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
		0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
		0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
		0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]

INV_S_BOX = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d

]
round_constants = [0x00000000, 0x01000000, 0x02000000,
		0x04000000, 0x08000000, 0x10000000, 
		0x20000000, 0x40000000, 0x80000000, 
		0x1b000000, 0x36000000]

const_matrix =  [
        [0x02, 0x03, 0x01, 0x01],
        [0x01, 0x02, 0x03, 0x01],
        [0x01, 0x01, 0x02, 0x03],
        [0x03, 0x01, 0x01, 0x02]
    ]

inv_const_matrix = [
    [0x0e, 0x0b, 0x0d, 0x09],
    [0x09, 0x0e, 0x0b, 0x0d],
    [0x0d, 0x09, 0x0e, 0x0b],
    [0x0b, 0x0d, 0x09, 0x0e]

]
def hex2Bin(hex_string):
	
	binary_string = bin(int(hex_string, 16)).lstrip('0b')

	return binary_string

def bin2Hex(binary_string):
	padded_binary_string = ''.join(['0' * (8 - len(byte)) + byte if len(byte) < 8 else byte for byte in binary_string.split()])

# Convert binary string to hexadecimal string
	hex_string = '{:X}'.format(int(padded_binary_string, 2))
	padded_hex_string = hex_string.zfill(len(hex_string) + len(hex_string) % 2)
	return padded_hex_string.lower()

def string2binary(text):
    return ''.join(format(ord(i), '08b') for i in text)

def image2binary(filename):
    with open(filename, 'rb') as fd:
        return ''.join([format(x, 'b') for x in fd.read()])

def splitString(text, size=128):
    text = [text[i:i+size] for i in range(0, len(text), size)]
    if len(text[-1]) < size:
        text[-1] += '0'*(size-len(text[-1]))
    return text

def s_box(word,box):
	subbedWord = ()

	for i in range(4):
		#using msb and lsb get the row and column in decimal form
		if word[i][0].isdigit() == False:
			row = ord(word[i][0]) - 86
		else:
			row = int(word[i][0])+1

		#repeat above for the seoncd char
		if word[i][1].isdigit() == False:
			col = ord(word[i][1]) - 86
		else:
			col = int(word[i][1])+1

		s_box_spot = (row*16) - (17-col) 

		new_val = hex(box[s_box_spot])[2:]

		if len(new_val) != 2:
			new_val = '0' + new_val
		subbedWord = (*subbedWord, new_val)
	return "".join(subbedWord)

def shift(curr_word):
    return curr_word[1:] + curr_word[:1]

def shift_right(curr_word):
    return curr_word[-1:] + curr_word[:-1]

def xor(num_1, num_2):
	bin_num_1 = bin(int(str(num_1), 16))
	bin_num_2 = bin(int(str(num_2), 16))
	

	xored = int(bin_num_1, 2) ^ int(bin_num_2, 2)
	

	new_hex = hex(xored)[2:]
	
	while len(new_hex) != 8:
		new_hex = '0' + new_hex
	return new_hex


def generate_words(given_key,size):
    #make empty list to hold amount of tuples based on size of key
	words = [()]*size
	for i in range(4):
		words[i] = (given_key[4*i], given_key[4*i+1], given_key[4*i+2],given_key[4*i+3])
	for i in range(4, size):
		tmp = words[i-1]
		word = words[i-4]
		
		if i % 4 == 0:
			rotated = shift(tmp)
			subbed = s_box(rotated,S_BOX)
			rcon = round_constants[int(i/4)]

			tmp = xor(subbed,hex(rcon)[2:])
		xored_val = xor("".join(word),"".join(tmp))
		words[i] = (xored_val[:2], xored_val[2:4], xored_val[4:6], xored_val[6:8])

	keys = []
	keys = [words[i:i+4] for i in range(0, len(words), 4)]
	return keys



def initializeStateArr(plaintext,stateArr):
	stateArr = [plaintext[i:i+4] for i in range(0, len(plaintext), 4)]

	return stateArr
	

def xorStateArrCol(currState,word,col_num):
	xored_col = xor("".join(word),"".join(currState[col_num]))
	if len(xored_col) < 8:
		xored_col = "0" + xored_col
	
	xored_arr =  [xored_col[i:i+2] for i in range(0, len(xored_col), 2)] 

	currState[col_num] = xored_arr
	return currState
	
def sub_cols(currState,box):
	for i in range(4):
		currCol = []
		currCol = s_box(currState[i],box)
		currState[i] = [currCol[j:j+2] for j in range(0, len(currCol), 2)] 
	return currState

def shift_rows(currState):
	rows = []
	for i in range(4):
		row = []
		for j in range(4):
			row.append(currState[j][i])
		rows.append(row)

	for i,row in enumerate(rows):
		for j in range(i):
			row = shift(row)
			rows[i] = row
	
	cols = []
	for i in range(4):
		col = []
		for j in range(4):
			col.append(rows[j][i])
		cols.append(col)
	return rows
	
def shift_rows_right(currState):
    rows = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(currState[j][i])
        rows.append(row)

    for i, row in enumerate(rows):
        for j in range(i):
            row = shift_right(row)
            rows[i] = row
    cols = []
    for i in range(4):
        col = []
        for j in range(4):
            col.append(rows[j][i])
        cols.append(col)
    return cols
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

def hex_to_int(val):
    return int(val, 16)

def int_to_hex(val):
    return hex(val)[2:].zfill(2)

def mix_single_column(a):
    # see Sec 4.1.2 in The Design of Rijndael
    t = hex_to_int(a[0]) ^ hex_to_int(a[1]) ^ hex_to_int(a[2]) ^ hex_to_int(a[3])
    u = hex_to_int(a[0])
    a[0] = int_to_hex(t ^ xtime(hex_to_int(a[0]) ^ hex_to_int(a[1])))
    a[1] = int_to_hex(t ^ xtime(hex_to_int(a[1]) ^ hex_to_int(a[2])))
    a[2] = int_to_hex(t ^ xtime(hex_to_int(a[2]) ^ hex_to_int(a[3])))
    a[3] = int_to_hex(t ^ xtime(hex_to_int(a[3]) ^ u))

def mix_columns(s):
    for i in range(4):
        mix_single_column(s[i])

def inv_mix_columns(s):
    for i in range(4):
        u = gMult_two(hex_to_int(s[i][0]), 0x0e) ^ gMult_two(hex_to_int(s[i][1]), 0x0b) ^ gMult_two(hex_to_int(s[i][2]), 0x0d) ^ gMult_two(hex_to_int(s[i][3]), 0x09)
        v = gMult_two(hex_to_int(s[i][0]), 0x09) ^ gMult_two(hex_to_int(s[i][1]), 0x0e) ^ gMult_two(hex_to_int(s[i][2]), 0x0b) ^ gMult_two(hex_to_int(s[i][3]), 0x0d)
        w = gMult_two(hex_to_int(s[i][0]), 0x0d) ^ gMult_two(hex_to_int(s[i][1]), 0x09) ^ gMult_two(hex_to_int(s[i][2]), 0x0e) ^ gMult_two(hex_to_int(s[i][3]), 0x0b)
        x = gMult_two(hex_to_int(s[i][0]), 0x0b) ^ gMult_two(hex_to_int(s[i][1]), 0x0d) ^ gMult_two(hex_to_int(s[i][2]), 0x09) ^ gMult_two(hex_to_int(s[i][3]), 0x0e)
        s[i][0] = int_to_hex(u)
        s[i][1] = int_to_hex(v)
        s[i][2] = int_to_hex(w)
        s[i][3] = int_to_hex(x)

    return s
def gMult(num, mult):
    if mult == 0x01:
        return num
    elif mult == 0x02:
        result = num << 1
        if num & 0x80:  # If MSB is 1, then it will overflow after left shift
            result ^= 0x1b  # XOR with the irreducible polynomial x^8 + x^4 + x^3 + x + 1
        return result & 0xFF  # Ensure only 8 bits
    elif mult == 0x03:
        return gMult(num, 0x02) ^ num
    elif mult == 0x09:
        return gMult(gMult(gMult(num, 0x02), 0x02), 0x02) ^ num
    elif mult == 0x0b:
        return gMult(gMult(gMult(num, 0x02), 0x02) ^ num, 0x02) ^ num
    elif mult == 0x0d:
        return gMult(gMult(gMult(num, 0x02) ^ num, 0x02), 0x02) ^ num
    elif mult == 0x0e:
        return gMult(gMult(gMult(num, 0x02) ^ num, 0x02) ^ num, 0x02)
		
def gMult_two(num,mult):
	binNum = format(num, '08b')
	if mult == 0x01:
		return num
	elif mult == 0x02:
		mask = 2 ** 8 - 1
		shiftedNum = (num << 1) & mask
		if binNum[0] == '0':
			return shiftedNum
		else:
			return (shiftedNum ^ 0b00011011)
	elif mult == 0x03:
		return (gMult(num, 0x02) ^ num)
	elif mult == 0x09:
		a = num
		for i in range(0, 3):
			a = gMult(a, 0x02)
		return (a ^ num)
	elif mult == 0x0b:
		a = num
		for i in range(0, 2):
			a = gMult(a, 0x02)
		a = a ^ num
		a = gMult(a, 0x02)
		return (a ^ num)
	elif mult == 0x0d:
		a = num
		a = gMult(a, 0x02)
		a = a ^ num
		for i in range(0, 2):
			a = gMult(a, 0x02)
		return (a ^ num)
	elif mult == 0x0e:
		a = num
		for i in range(0, 2):
			a = gMult(a, 0x02)
			a = a ^ num
		return (gMult(a, 0x02))
	
def mix(currState):
	newState  =[]

	for i in range(4):
		newState.append(currState[i])

	for j in range(0,4):
		newCol = [0,0,0,0]
		currCol = [newState[0][j],newState[1][j],newState[2][j],newState[3][j]]
		for row in range(0,4):
			for col in range(0,4):
				newCol[row] ^= gMult(int(currCol[col], 16), const_matrix[row][col])
			for k in range(0,4):
				newState[k][j] =  "0x{:02x}".format(newCol[k])
	return newState
def invMix(currState):
    newState = [[0] * 4 for _ in range(4)]  # Initialize the new state with zeros
    
    for j in range(4):
        for row in range(4):
            for col in range(4):
                newState[row][j] ^= gMult(int(currState[col][j], 16), inv_const_matrix[row][col])
    hex_strings = [[hex(val)[2:].zfill(2) for val in sublist] for sublist in newState]
    return hex_strings

def invMix_two(currState):
    newState = []

    for i in range(4):
        newState.append(currState[i])

    for j in range(0, 4):
        newCol = [0, 0, 0, 0]
        currCol = [newState[0][j], newState[1][j], newState[2][j], newState[3][j]]
        for row in range(0, 4):
            for col in range(0, 4):
                newCol[row] ^= gMult(int(currCol[col], 16), inv_const_matrix[row][col])
            for k in range(0, 4):
                newState[k][j] = "0x{:02x}".format(newCol[k])
    return newState


def rowsToCols(currState):
	cols = []
	for i in range(4):
		col = []
		for j in range(4):
			if (len(currState[j][i]) > 2):
				col.append((currState[j][i])[2:])
			else:
				col.append((currState[j][i]))
		cols.append(col)
	return cols

def aes_decrypt(key,ciphertext,inputType='Binary'):
	key = bin2Hex(key)
	binary = ciphertext
	if inputType == 'Text':
		binary = string2binary(ciphertext)
	if inputType == 'File':
		binary = image2binary(ciphertext)
	if len(binary) > 64:
		binary = splitString(binary)
	decrypted = ""
	for b in binary:
		plaintext_hex = bin2Hex(b)
		plaintextArr = [plaintext_hex[i:i+2] for i in range(0, len(plaintext_hex), 2)]
		keyArr = [key[i:i+2] for i in range(0, len(key), 2)]

		keys = generate_words(keyArr,44)
		currState = []
		stateArr = initializeStateArr(plaintextArr,currState)
	
		for i in range(4):
			stateArr = xorStateArrCol(stateArr,keys[-1][i],i)
		for r in range(9,0,-1):
			stateArr = shift_rows_right(currState=stateArr)
			stateArr = sub_cols(stateArr,INV_S_BOX)
			for i in range(4):
				stateArr = xorStateArrCol(stateArr,keys[r][i],i)
			stateArr = inv_mix_columns(stateArr)	
			
		stateArr = shift_rows_right(stateArr)
		stateArr = sub_cols(stateArr,INV_S_BOX)
		for i in range(4):
			stateArr = xorStateArrCol(stateArr,keys[0][i],i)

			


		b_decrypt = ""
		for col in stateArr:
			for item in col:
				b_decrypt = b_decrypt + item
		decrypted = decrypted + b_decrypt
	return hex2Bin(decrypted)

		
		
		



def main():

	#key = "5468617473206d79204b756e67204675"
	#cipher_text = "29c3505f571420f6402299b31a02d73a"
	key = "00101011011111100001010100010110001010001010111011010010101001101010101111110111000101011000100000001001110011110100111100111100"
	cipher_bin = "00111001001001011000010000011101000000101101110000001001111110111101110000010001100001011001011100011001011010100000101100110010"
	stateArr = aes_decrypt(key,cipher_bin,inputType='binary')



if __name__ == '__main__':
	main()
