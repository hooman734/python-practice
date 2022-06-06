"""
Question 2

Ask the user to press any key.
Display any 3 random space-separated digits between 0-9 e.g. 6 2 7.
If any of them is 7, output "Congratulations!".
Else, output "Try again! Better luck next time.".
"""


import random 


def lottery():
    number_of_attempts = 3
    list_of_numbers: list = []

    for i in range(number_of_attempts):
        seed = input("Press Any Key And Then Hit The Enter!")
        random.seed(seed)
        list_of_numbers.append(random.randint(0, 9))

    if 7 in list_of_numbers:
        print("\nCongratulations!")
    else:
        print("\nTry again! Better luck next time.")


if __name__ == '__main__':
    lottery()
