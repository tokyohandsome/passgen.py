"""
This script generates a password, by default, length is 12 characters.
Password length and special characters can be modified by options.

Usage:
python3 passgen.py [option1] [option2]
option1 can be a number of characters e.g. 8, 20, etc.
option2 can be either - (minus, remove special characters) or a string of special caracters in quotes e.g. '!@#$%^', '-_', etc.
"""
import string
import secrets
import sys

def passgen(len_pw, punctuation = string.punctuation):
    letters = string.ascii_letters
    digits = string.digits

    return(''.join(secrets.choice(punctuation + letters + digits) for i in range(len_pw)))

def main():
    # check arguments
    if len(sys.argv) >= 2:
        # if option1 is NOT an intiger, set the password length to 12.
        try:
            len_pw = int(sys.argv[1])
        except ValueError:
            len_pw = 12
        # if option2 exists and it is '-' remove special character otherwise pass it as a list of special characters.
        if len(sys.argv) == 3:
            if sys.argv[2] == '-':
                password = passgen(len_pw, '')
            else:
                password = passgen(len_pw, sys.argv[2])
        else:
            password = passgen(len_pw)
    else:
        password = passgen(12)

    print(password)

if __name__ == '__main__':
    main()
