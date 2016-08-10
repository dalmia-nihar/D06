import os
def list_files():
    os.chdir("C:\\Users\\Dell\\pbc2016\\D06")
    print("Path: " + os.getcwd())
    print("Files are:")
    for file_name in os.listdir():
        if file_name.endswith(".py"):
            print(file_name)

def main():
    list_files()


if __name__ == "__main__":
    main()