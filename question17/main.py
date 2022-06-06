"""
Question17 - Convert Decimal to Base n

Write a program to convert from decimal (base 10) to base n.
Request the value of n.
Request the decimal value.
Convert to base n, and output the result.
"""


import numbers 
import string 
import re 


def convert_to_decimal(input_number, base):
    alphanumerical_list = {'A': 10,
                           'B': 11,
                           'C': 12,
                           'D': 13,
                           'E': 14,
                           'F': 15,
                           'G': 16,
                           'H': 17,
                           'I': 18,
                           'J': 19,
                           'K': 20,
                           'L': 21,
                           'M': 22,
                           'N': 23,
                           'O': 24,
                           'P': 25,
                           'Q': 26,
                           'R': 27,
                           'S': 28,
                           'T': 29,
                           'U': 30,
                           'V': 31,
                           'W': 32,
                           'X': 33,
                           'Y': 34,
                           'Z': 35}

    number = re.findall(r'\d|[A-Z]', str(input_number).strip().upper())

    base = str(base).strip()
    if int(base) < 2 or not base.isdecimal():
        raise Exception("The Base is Invalid!")
    else:
        base = int(base)

    output: numbers = 0

    for i in range(len(number)):
        digit: string = number[-1 - i]

        if digit.isupper():
            digit = int(alphanumerical_list[digit])
        else:
            digit = int(digit)

        if digit >= base:
            raise Exception("The Input Number is Invalid!")

        output += int(digit) * base ** i

    print(f"The Input Number ({input_number} in base {base}) in Decimal is {output}")


if __name__ == '__main__':
    convert_to_decimal("A157BC019K", 50)
