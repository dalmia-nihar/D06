import os

def read_write_e():
	count = 0
	lst_names = []
	with open("roster.txt", "r") as f:
		for s in f:
			name = s.split()[0]
			if 'e' in name :
				count += 1
				lst_names.append(name)
	
	f2 = open("D06ex04.txt", "w")
	f2.write("Number of Names with 'e' > ")
	f2.write(str(count))
	f2.write("\nNames with 'e' > ")
	f2.write(repr(lst_names))


def main():
	read_write_e()

if __name__ == "__main__":
	main()



