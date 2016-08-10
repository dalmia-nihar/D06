# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()




def nested_sum(lst):
	list_sum = 0
	for i in range(len(lst)):
		if type(lst[i]) is list: 
			list_sum += nested_sum(lst[i])
		else:
			list_sum += lst[i]
	return list_sum

##############################################################################
def main():
	sample1 = [1,2,3,[4,5]]
	print("The sum of the list: " + repr(sample1) + " is: " + str(nested_sum(sample1)))
	sample2 = [[1,2],3,[4,5]]
	print("The sum of the list: " + repr(sample2) + " is: " + str(nested_sum(sample2)))
	sample3 = [[[1,2],3],4,5]
	print("The sum of the list: " + repr(sample3) + " is: " + str(nested_sum(sample3)))
	sample4 = [1,2,3,4,5]
	print("The sum of the list: " + repr(sample4) + " is: " + str(nested_sum(sample4)))

if __name__ == '__main__':
    main()
