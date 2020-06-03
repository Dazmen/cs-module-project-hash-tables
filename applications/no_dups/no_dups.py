def no_dups(s):
    # Your code here
    words = s.split(' ')

    word_cache = {}

    for word in words:
        if word not in word_cache:
            word_cache[word] = word
    
    new_words_list = []

    for word in word_cache:
        new_words_list.append(word)

    new_string = " "

    new_string = new_string.join(new_words_list)
    return new_string

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))