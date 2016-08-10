#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports
import sys
import os
# Body


def avoids(wrd,st):
    """ return True if word NOT forbidden"""
    for letter in st:
        if letter in wrd: 
            return False
    return True

def print_forbidden(s):
    with open("words.txt", "r") as f:
        count = 0
        for name in f:
            if avoids(name.strip(), s):
                count += 1
        print("Number of words that are not forbidden are: " + str(count))



def forbidden_prompt():
    """ print count of words NOT forbidden by input"""
    forbid_str = input("Please enter list of forbidden chars: ")
    print_forbidden(forbid_str)



def forbidden_param():
    """ return count of words NOT forbidden by param"""
    if len(sys.argv) == 2:
        print_forbidden(sys.argv[1])



def find_five():
    ...


##############################################################################
def main():
    # Your final submission should only call five_five
    forbidden_param()


if __name__ == '__main__':
    main()
