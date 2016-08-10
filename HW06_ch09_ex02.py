#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body
def has_no_e(s):
	if 'e' in s:
		return False
	else: 
		return True

def print_no_e():
	no_e_count = 0
	total_count = 0
	with open("words.txt", "r") as f:
		for s in f:
			total_count += 1
			if has_no_e(s.strip()) :
				no_e_count += 1
				print(s.strip())
				
	print("Number of Names without 'e' > " + str(no_e_count))
	print("Total Number of Names > " + str(total_count))
	print("Percentage of no e's > " + str(no_e_count * 100 / total_count))


##############################################################################
def main():
    print_no_e()  # Call your function(s) here.

if __name__ == '__main__':
    main()
