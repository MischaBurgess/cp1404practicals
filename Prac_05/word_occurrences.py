"""
Word Occurrences Task
Mischa Burgess
"""
words = input("Enter your words: ")
words = words.split()  # split input
word_dict = {}  # create empty dictionary
for word in words:
    if word in word_dict:
        word_dict[word] += 1  # count words
    else:
        word_dict[word] = 1  # if word doesn't appear again, count = 1

words = list(word_dict.keys())  # make a word list
words.sort()  # sort the word list

max_word_length = len(max(words, key=len))  # finds longest word entered to ensure correct spacing
for word in words:
    print("{:{}} : {}".format(word, max_word_length, word_dict[word]))  # prints result with correct spacing
