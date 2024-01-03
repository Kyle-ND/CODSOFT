import string
import random
import pyfiglet
import os

def main():
    #main part of the program where the magic happens :)

    possible_chars = characters()
    f = pyfiglet.figlet_format("Password Generator", font="slant")
    print(f)
    name = input("Enter your name: ")
    length = get_length()
    running = True

    while running:

        password = ''
        for _ in range(length):
            password += random.choice(possible_chars)

        print(f"Password: {password}")
        response = input("Regenerate (Y/N)?: ").upper()

        if response == 'Y':
            os.system("cls")
            f = pyfiglet.figlet_format("Password Generator", font="slant")
            print(f)

        else:
            print(f"Password: {password}")
            running = False


def get_length():
    #get valid number as length of the password

    while True:
        try:
            length = int(input("how long would you want your password to be: "))
            return length
        except ValueError:
            print("please enter a valid number!")


def characters():
    #using string module create a list with all possible characters for a password 

    invalid_chars = ["{","}",")","(",":","<",">","[","]","|","/","=","'","+","-",]
    letters = list(string.ascii_letters)
    digits = list(string.digits)
    special_characters = list(filter(lambda x : x not in invalid_chars,list(string.punctuation)))

    return letters + digits + special_characters


if __name__ == "__main__":
    main()