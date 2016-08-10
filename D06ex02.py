import os
import random

def write_file():
	with open("write_ex02.txt", "w") as f:
		for i in range(10):
			f.write(str(random.randint(0,100)) + "\n")
	f.close()
			
def main():
	write_file()

if __name__ == "__main__":
	main()


