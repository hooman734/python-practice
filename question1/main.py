"""
Question 1 - Name Concatenation

Request the user's first name, last name and age.
Print out Welcome, <First-Name> <Last-Name> (<Age>) in a new line. See Variants.
"""


import numbers
import string


def name_concatenation():
    user_name: string = input("User Name?").capitalize()
    last_name: string = input("Last Name?").capitalize()
    age: numbers = input("age?")

    if user_name.isalpha() and last_name.isalpha() and age.isnumeric():
        print(f"Welcome, {user_name} {last_name} ({age})")

    else:
        print("Wrong Input Format!")


if __name__ == '__main__':
    name_concatenation()
