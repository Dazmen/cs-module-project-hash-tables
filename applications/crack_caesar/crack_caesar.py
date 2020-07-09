import re
# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
def build_decode_key(encoded_arr):
    # the frequency_list array is ordered from most frequent(index[0]) to least(index[25])
    # this will map to the sorted frequencies of characters in the encoded_array
    # loop through and create a hash table with the key being from encoded_arr[i] and the value being frequency_list[i] to create the decoding hashtable
    frequency_list = ['E', 'T', 'A', 'O', 'H', 
                    'N', 'R', 'I', 'S', 'D', 
                    'L', 'W', 'U','G', 'F', 
                    'B', 'M', 'Y', 'C', 'P', 
                    'K', 'V', 'Q', 'J', 'X', 'Z']
    decode_key = {}

    for i in range(len(frequency_list)):
        key = encoded_arr[i][0] # the 0 index is selecting the character as the key (leaving out the frequency)
        value = frequency_list[i]
        if key not in decode_key:
            decode_key[key] = value

    for l in decode_key:
        print(f'Key: {l}, Value: {decode_key[l]}')

    return decode_key


def decode(txt):
    total_letter_count = 0
    encoded_letter_cache = {}

    hacky_removal = ['\t', '\r', '\n']

    for annoying_regex in hacky_removal: # why does this work but a list of illegal chars threw me an error?
        string = txt.replace(annoying_regex, " ")

    new_string = re.sub(r'[^a-zA-Z]', '', string)

    for char in new_string:
        if char not in encoded_letter_cache and len(char) > 0:
            encoded_letter_cache[char] = 1
            total_letter_count += 1
        elif len(char) > 0:
            encoded_letter_cache[char] += 1
            total_letter_count += 1

    # encoded_letter_cache now contains all the letters in the cipher and how many times they occur
    # next step is to get the frequency, turn it into a list and sort it.

    for letter in encoded_letter_cache:
        encoded_letter_cache[letter] = encoded_letter_cache[letter] / total_letter_count

    encoded_letters = list(encoded_letter_cache.items())
    encoded_letters.sort(key=lambda l: l[1], reverse=True)
  
    decode_key = build_decode_key(encoded_letters) # dict with encoded keys and decoded values

    # Decode the text
    decoded_txt = ''
    
    for c in txt:
        if c in decode_key:
            decoded_char = c.replace(c, decode_key[c])
            decoded_txt = decoded_txt + decoded_char
        else:
            decoded_txt = decoded_txt + c
    
    print(decoded_txt)
    return decoded_txt

with open("ciphertext.txt") as f:
    words = f.read()
    decode(words)