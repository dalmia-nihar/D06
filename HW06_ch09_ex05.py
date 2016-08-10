#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: [type here]
#   - # of words that use all aeiouy: [type here]
##############################################################################
# Imports

import os

# Body
def uses_all(wrd,st):
    for letter in st:
        if letter not in wrd: 
            return False
    return True

def word_count(s):
    with open("words.txt", "r") as f:
        count = 0
        for name in f:
            if uses_all(name.strip(), s):
                count += 1
        print("Number of words that contain all of " + s + " are :" + str(count))



##############################################################################
def main():
    word_count("aeiou")
    word_count("aeiouy")

if __name__ == '__main__':
    main()
