"""
Question14 - Number in Words

Ask the user to enter a number.
Print out the entered number in words.
E.g. 30,456 becomes "Thirty thousand, four hundred and fifty six".
"""


import re 


def number_in_words(number):
    to_show_number = "".join(
        list(reversed(",".join(re.findall(r'\d{3}|\d{2}|\d', "".join(list(reversed(str(number)))))))))
    alphanumerical_numbers = {0: "",
                              1: "one",
                              2: "two",
                              3: "three",
                              4: "four",
                              5: "five",
                              6: "six",
                              7: "seven",
                              8: "eight",
                              9: "nine",
                              10: "ten",
                              11: "eleven",
                              12: "twelve",
                              13: "thirteen",
                              14: "fourteen",
                              15: "fifteen",
                              16: "sixteen",
                              17: "seventeen",
                              18: "eighteen",
                              19: "nineteen",
                              20: "twenty",
                              30: "thirty",
                              40: "forty",
                              50: "fifty",
                              60: "sixty",
                              70: "seventy",
                              80: "eighty",
                              90: "ninty",
                              100: "hundred",
                              1000: "thousand",
                              1000000: "million",
                              1000000000: "billion",
                              1000000000000: "trillion",
                              1000000000000000: "quadrillion",
                              1000000000000000000: "quintillion",
                              1000000000000000000000: "sextillion",
                              1000000000000000000000000: "septillion",
                              1000000000000000000000000000: "octillion",
                              1000000000000000000000000000000: "nonillion",
                              1000000000000000000000000000000000: "decillion"}

    def say_number_under_thousand(input_number):
        input_number = int(input_number)
        if input_number < 20:
            return f"{alphanumerical_numbers[input_number].capitalize()}"
        elif input_number < 100:
            _last_digit_ = input_number % 10
            _tens_digit_ = int(input_number / 10)
            return f"{alphanumerical_numbers[_tens_digit_ * 10].capitalize()} {alphanumerical_numbers[_last_digit_].capitalize()}"
        _2_last_digits_ = input_number % 100
        _hundreds_digit_ = int(input_number / 100)
        if_and = "" if _2_last_digits_ == 0 else " and "
        return f"{alphanumerical_numbers[_hundreds_digit_].capitalize()} {alphanumerical_numbers[100].capitalize()}{if_and}{say_number_under_thousand(_2_last_digits_)}"

    output = ""
    factor = 1
    chunks_of_numbers = to_show_number.split(",")[::-1]

    for split_number in chunks_of_numbers:
        split_number = int(split_number)
        suffix = "" if int(split_number) == 0 else f" {alphanumerical_numbers[factor].capitalize()}, "
        output = f"{say_number_under_thousand(split_number) if factor < 1000 else f'{say_number_under_thousand(split_number)}{suffix}'}" + output
        factor *= 1000
    output = f"{re.split(r', $', output)[0]}."
    print(f"The number ({to_show_number}) is: {output}")


if __name__ == '__main__':
    number_in_words(30456)