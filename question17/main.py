"""
Question17 - Convert Decimal to Base n

Write a program to convert from decimal (base 10) to base n.
Request the value of n.
Request the decimal value.
Convert to base n, and output the result.
"""


import numbers 


def convert_decimal_to_base_n(decimal_number, base_n):
    numerator: numbers = int(decimal_number)
    denominator: numerator = int(base_n)
    output: list = []

    while numerator >= denominator:
        calculate = numerator % denominator
        output.insert(0, str(calculate))
        numerator = int(numerator / denominator)

    output.insert(0, str(numerator))

    print(" ".join(output))


if __name__ == '__main__':
    convert_decimal_to_base_n(1024, 2)