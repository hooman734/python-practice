"""
Question5 - Temperature Unit Conversion

Output:

1. Celsius to Fahrenheit
2. Fahrenheit to Celsius

Enter an option:
If the user enters 1, ask the user to "Enter a celsius value:".
Else, ask the user to "Enter a Fahrenheit value:".
Convert the entered value to celsius or fahrenheit accordingly.
"""


import numbers 
import string 


def temp_unit_conv():
    if_conv_from_cel_to_fah: bool
    input_temp: numbers
    output_temp: numbers
    output: string
    check = input("Enter 1 to Input in Celsius: \n")

    if check == '1':
        input_temp = input("Enter a celsius Value: ")
        output_temp = 1.8 * float(input_temp) + 32
        output = "The Temperature in Fahrenheit is: {:.3f}"
    else:
        input_temp = input("Enter a Fahrenheit Value: ")
        output_temp = (float(input_temp) - 32) / 1.8
        output = "The Temperature in Celsius is: {:.3f}"

    print(output.format(output_temp))


if __name__ == '__main__':
    temp_unit_conv()