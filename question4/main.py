"""
Question 4 - Type in Reverse

Output a random word. Ask the user to type in the reverse.
If the user is correct, output white_check_mark
Else, output x
"""


import numbers 
import random 
import string 


def type_in_reversed():
    alphabet: list = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
    length_of_random_word: numbers = 5
    random_word: string = ""
    stack: list = []
    reversed_random_word: string = ""

    for i in range(length_of_random_word):
        index = random.randint(0, 30)
        if index < 26:
            character: char = alphabet[index]
        else:
            character = " "
        random_word += character

    random_word = random_word.strip()
    print(f"Please Write this in Reverse --> ({random_word})")

    for character in random_word:
        stack.append(character)

    for i in range(len(random_word)):
        reversed_random_word += stack.pop()

    # for i in range(len(reversed_random_word)):
    #     character = reversed_random_word[i]
    #     check = input(": ")
    #     if check != character and character != " ":
    #         print("Failed!")
    #         break
    #     if character == reversed_random_word[-1]:
    #         print("Well Done!")

    check_word = input()

    if check_word == reversed_random_word:
        print("Well Done!")
    else:
        print("Failed!")

    
if __name__ == '__main__':
    type_in_reversed()
