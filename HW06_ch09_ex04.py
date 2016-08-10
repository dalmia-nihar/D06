#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1:
#       2:
#       3:
##############################################################################
# Imports

import os

# Body
def uses_only(wrd,st):
    for letter in wrd:
        if letter not in st: 
            return False
    return True

def print_sentence():
    with open("words.txt", "r") as f:
        for name in f:
            if uses_only(name.strip(), "acefhlo"):
                print(name.strip(), end = " ")
    print(".")
        


##############################################################################
def main():
    print_sentence()  # Call your function(s) here.

if __name__ == '__main__':
    main()
