import re

# Note: I think I despise regex/regular expression.....

def word_count(s):
    # Your code here
    word_cache = {}

    hacky_removal = ['\t', '\r', '\n']

    for annoying_regex in hacky_removal: # why does this work but a list of illegal chars threw me an error?
        s = s.replace(annoying_regex, " ")

    new_string = re.sub(r'[^a-zA-Z\'\s]', '', s)

    words = new_string.split(' ')

    for word in words:
        if word.lower() not in word_cache and len(word) > 0:
            word_cache[word.lower()] = 1
        elif len(word) > 0:
            word_cache[word.lower()] += 1

    print('HELLO', word_cache)
    return word_cache
    

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))