##### WHY IS THIS ALL REGEX
import re
# Your code here

def moreRegex(txt):
    word_cache = {} 

    hacky_removal = ['\t', '\r', '\n']

    for annoying_regex in hacky_removal:
        txt = txt.replace(annoying_regex, " ")

    new_string = re.sub(r'[^a-zA-Z\'\s]', '', txt)

    words = new_string.split(' ')
 
    longest_word = '' # to keep track of the longest word for disaply purposes

    for word in words:
        if word.lower() not in word_cache and len(word) > 0:
            word_cache[word.lower()] = 1
            if len(word) > len(longest_word):
                longest_word = word
        elif len(word) > 0:
            word_cache[word.lower()] += 1
    
    word_list = list(word_cache.items()) # turn the word_cache into a list of tuples
    word_list.sort() #Sort first alpha
    word_list.sort(key=lambda w: w[1], reverse=True) # then sort by count value

    for word in word_list:
        histograph = '#' * word[1] # declare a variable representing one '#' per count of a word
        print(f'{word[0]:{len(longest_word) + 3}} {histograph}')


with open("robin.txt") as f:
    words = f.read()
    moreRegex(words)



## Planning

# function takes a .txt file

# declare a word cache, the word being the key, the count representing how many '#' will be printed
#### just import/copy+paste the word count function?

# sort the obj keys when printing by count then alphabetically

# Ignore case (output lowercase, just make key'txt lowercase




# Return to the justified bit.....later not a concern currently
