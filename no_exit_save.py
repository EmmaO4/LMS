def overwrite_file():
    with open("Exercises/no_save.txt", "w") as file:
        file.write("new file line")

def append_file():
    with open("Exercises/no_save.txt", "a") as file:
        file.write("\nappending line")

def modify_first_line(new_text):
    try:
        with open("Exercises/no_save.txt", "r") as file:
            lines = file.readlines()

            if not lines:
                print("File is empty")

            if lines:
                lines[0] = new_text.rstrip("\n") + "\n"

        with open("Exercises/no_save.txt", "w") as file:
            file.writelines(lines)
    except FileNotFoundError:
        print("File not found")

def main():
    # overwrite_file()    
    #append_file()
    user_input = input()
    modify_first_line(user_input)
    with open("Exercises/no_save.txt", "r") as file:
        print(file.read())

if __name__ == "__main__":
    main()
