import sys

#Example round key expansion in hex, 128 bit 
#Round key 0: 54 68 61 74 73 20 6D 79 20 4B 75 6E 67 20 46 75
#Round key 1: E2 32 FC F1 91 12 91 88 B1 59 E4 E6 D6 79 A2 93
#Round Key 2: 56 08 20 07 C7 1A B1 8F 76 43 55 69 A0 3A F7 FA




S_BOX = [
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
originalKey = originalKey.upper()
round_keys = [0 for x in range(10)]
round_keys[0] = originalKey
#Pattern for left shifts in bytes for 128 bit key
left_shifts_one = [1,2,4,8,16,32,64,128,27,54]

#Function to perform left circular shift
def circular_shift_hex(hex_number, shift_bytes):
    # Convert hex number to binary string
    binary_string = bin(int(hex_number, 16))[2:]

    # Ensure the binary string has a length that is a multiple of 4
    binary_string = binary_string.zfill(len(hex_number) * 4)

    # Perform circular shift
    shifted_binary = binary_string[shift_bytes * 8:] + binary_string[:shift_bytes * 8]

    # Convert the shifted binary string back to hexadecimal
    shifted_hex = hex(int(shifted_binary, 2))[2:]

    # Ensure the resulting hex string has the same length as the input hex number
    shifted_hex = shifted_hex.zfill(len(hex_number))

    return shifted_hex.upper()
#Function to split key string into "words" or 4, 4 byte words
def create_words(full_key):
    words = [full_key[i:i+8] for i in range(0, len(full_key),8)]
    return words


#Function to generate a key based on its index (uses the previous key as well)
def generate_next_key(index):
    words = create_words(round_keys[index-1]) 
    print(f"words: {words} ")
    #step 1: perform left circular shift on previous key
    rotated_key = "".join([circular_shift_hex(word, left_shifts_one[index-1]) for word in words])  
    print(f"rotated key: {rotated_key}")
    rotated_bytes = [rotated_key[i:i+2] for i in range(0, len(rotated_key), 2)]
    #Each byte msb and lsb represent row and column in s-box table, then take that value and replace it
    s_substitution =[(S_BOX[int(byte[0],16)][int(byte[1],16)]) for byte in rotated_bytes]
    print(f"subbed key: {s_substitution}")
    #Split into words again
    subbed_words = create_words("".join(s_substitution))
    print(f"subbed words: {subbed_words}")
  
    # Define round constants for AES, numbers in hex to be xored with the fourth word in the key
    round_constants = [
        "01000000",
        "02000000",
        "04000000",
        "08000000",
        "10000000",
        "20000000",
        "40000000",
        "80000000",
        "1B000000",
        "36000000"
    ]
    #xor the fourth word with the round constant for this round
    new_word_3 = hex(int(subbed_words[3], 16) ^ int(round_constants[index-1], 16))[2:].zfill(8)
    #XOR this the fourth word, or word 3 original word 0 to create word 4, then xor word four and word 1 to get word 5, xor word 5 and word 2 to get word 6 etc
    word_4 = hex(int(words[0], 16) ^ int(new_word_3, 16))[2:].zfill(8)
    word_5 = hex(int(words[1], 16) ^ int(word_4, 16))[2:].zfill(8)
    word_6 = hex(int(words[2], 16) ^ int(word_5, 16))[2:].zfill(8)
    word_7 = hex(int(words[3], 16) ^ int(word_6, 16))[2:].zfill(8)
    #words 4, 5, 6 and 7 make up the next round key 
    new_key = "".join([word.upper() for word in [word_4, word_5, word_6, word_7]])
    round_keys[index] = new_key
    
    

   


generate_next_key(1)

generate_next_key(2)

print(round_keys)


