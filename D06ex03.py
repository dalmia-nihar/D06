import os

def finding_e():
	count = 0
	lst_names = []
	with open("roster.txt", "r") as f:
		for s in f:
			name = s.split()[0]
			if 'e' in name :
				count += 1
				lst_names.append(name)
				
	print("Number of Names with 'e' > " + str(count))
	print("Names with 'e' > ")
	print(lst_names)


def main():
	finding_e()

if __name__ == "__main__":
	main()



