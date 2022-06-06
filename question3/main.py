"""
Question 3 - Word in Reverse

Ask the user to enter a word.

Print out the word in reverse.
"""


import string 


def word_in_reverse():
    sample_word: string = input("Input a Word To Be Reversed!")
    stack: list = []
    output: string = ""

    for letter in sample_word:
        stack.append(letter)

    for i in range(len(stack)):
        output += stack.pop()

    print(output)


if __name__ == '__main__':
    word_in_reverse()