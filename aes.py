import sys




#Example round key expansion in hex, 128 bit 
#Round key 0: 54 68 61 74
#  73 20 6D 79
#  20 4B 75 6E 
# 67 20 46 75
#Round key 1: E2 32 FC F1 
# 91 12 91 88 
# B1 59 E4 E6
#  D6 79 A2 93
#Round Key 2: 56 08 20 07 
# C7 1A B1 8F
#  76 43 55 69 
# A0 3A F7 FA
#Round 3: D2 60 0D E7 
# 15 7A BC 68 
# 63 39 E9 01 
# C3 03 1E FB


def xor_hex(hex_str_one,hex_str_two):
    a = bin(int(hex_str_one.upper(), 16))[2:].zfill(16)
    b = bin(int(hex_str_two.upper(), 16))[2:].zfill(16)
    binArr = [int(a1) ^ int(b1) for a1, b1 in zip(a, b)]
    binary_string = ''.join(map(str, binArr))
    
    # Pad the binary string if necessary
    padded_binary_string = binary_string.ljust((len(binary_string) + 7) // 8 * 8, '0')
    
    # Split the binary string into 8-bit chunks
    chunks = [padded_binary_string[i:i+8] for i in range(0, len(padded_binary_string), 8)]
    
    # Convert each chunk to hexadecimal and store in a list
    hex_bytes = [hex(int(chunk, 2))[2:].zfill(2) for chunk in chunks]
    
    return hex_bytes
    

def xor_binary_hex(hex_str_one,bin_num):
    b = bin(int(hex_str_one, 16))[2:].zfill(32)
    return [int(a1) ^ int(b1) for a1, b1 in zip(bin_num, b)]

roundConst = [0x00000000, 0x01000000, 0x02000000,
		0x04000000, 0x08000000, 0x10000000, 
		0x20000000, 0x40000000, 0x80000000, 
		0x1b000000, 0x36000000]
        
def sub(word):
    return[(S_BOX[int(byte[0],16)][int(byte[1],16)]) for byte in word]
S_BOX =[
    # Row 0
    ["63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76"],
    # Row 1
    ["CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0"],
    # Row 2
    ["B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15"],
    # Row 3
    ["04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75"],
    # Row 4
    ["09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84"],
    # Row 5
    ["53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "CF"],
    # Row 6
    ["D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8"],
    # Row 7
    ["51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2"],
    # Row 8
    ["CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73"],
    # Row 9
    ["60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB"],
    # Row 10
    ["E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79"],
    # Row 11
    ["E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08"],
    # Row 12
    ["BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A"],
    # Row 13
    ["70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1", "1D", "9E"],
    # Row 14
    ["E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55", "28", "DF"],
    # Row 15
    ["8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54", "BB", "16"]
]


originalKey = '5468617473206D79204B756E67204675'
secondKey = "E232FCF191129188B159E4E6D679A293"
originalKey = originalKey.upper()
round_keys = [0 for x in range(10)]
round_keys[0] = originalKey
round_keys[1] = secondKey
#Pattern for left shifts in bytes for 128 bit key
left_shifts_one = [1,2,4,8,16,32,64,128,27,54]

#Function to perform left circular shift
def circular_shift_hex(hex_word):
    return hex_word[1:] + hex_word[:1]
    '''  # Convert hex number to binary string
    binary_string = bin(int(hex_word, 16))[2:]

    # Ensure the binary string has a length that is a multiple of 4
    binary_string = binary_string.zfill(len(hex_word) * 4)

    # Perform circular shift
    shifted_binary = binary_string[8:] + binary_string[:8]

    # Convert the shifted binary string back to hexadecimal
    shifted_hex = hex(int(shifted_binary, 2))[2:]

    # Ensure the resulting hex string has the same length as the input hex number
    shifted_hex = shifted_hex.zfill(len(hex_word))'''
  

    return shifted_hex




#Function to generate a key based on its index (uses the previous key as well)
def generate_keys(key,size):
    allWords = [[]]*size #array of arrays representing each of the words needed, size varies based on key length (ie; 44 for 128)
     
    for i in range(4):
        allWords[i] = [key[4*i], key[4*i+1], key[4*i+2], key[4*i+3]]



    #fill out all the words 

    for wordCount in range (4,size):
        print()
        print(wordCount)
        #prior words that are needed
        tmp = allWords[wordCount -1]
        word = allWords[wordCount -4]
        print(f"tmp #1: {tmp}")
        print(f"word #1: {word}")

        #if multiple of 4, the rotation and substitution, and round const xoring occurs
        
        if wordCount % 4 == 0:
            #send to function to rotate word
            x = circular_shift_hex(tmp)
            print(f"x #1: {x}")
        
            #send to sbox to make substitutions
            y = sub(x)
            print(f"y #1: {y}")
            rcon = roundConst[int(wordCount/4)]
            print(f"rcon: {roundConst}")
        
            tmp = xor_hex("".join(y), "".join(hex(rcon)[2:]))
            print(f"tmp #2: {tmp}")
        word = ''.join(word)
        print(f"word #2: {word}")
  
        tmp = ''.join(tmp)
        print(f"tmp #3: {tmp}")
        xored = xor_hex (word, tmp)
        print(f"xored: {xored}")
 
        allWords[wordCount] = xored
    return allWords

    

def main():
    key = ["54", "68", "61", "74", "73", "20", "6d", "79", "20", "4b", "75", "6e", "67", "20", "46", "75"]

    #get key expansion
    keyWords = generate_keys(key,44)

    print("Key provided: " + "".join(key))
    print("\n\nKeywords: \n")
    for word in keyWords:
        print(word)
    for i in range(len(keyWords)):
	    print("w" + str(i), "=", keyWords[i][0], keyWords[i][1], keyWords[i][2], keyWords[i][3])


if __name__ == '__main__':
	main()
