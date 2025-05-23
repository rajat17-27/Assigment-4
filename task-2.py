


def write_to_file():
        with open("output.txt", "w") as file:
            user= input("Enter text to write: ")
            file.write(user)
        print("Your input has been written to output.txt.")


def append_to_file():
        with open("output.txt", "a") as file:
            user = input("Enter additional text to append: ")
            file.write("\n" + user)
        print("Your input has been appended to output.txt.")


def read_file():
        with open("output.txt", "r") as file:
            content = file.read()
        print("\nFinal content of output.txt:\n")
        print(content)



write_to_file()
append_to_file()
read_file()
