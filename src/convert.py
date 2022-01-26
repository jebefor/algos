from typing import Union


def to_decimal(number: Union[int, str], base: int) -> int:
    highest_digit_exp = len(str(number)) - 1
    decimal_number = 0

    hex_mappings = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

    for digit in str(number):
        if base == 16:
            if digit in hex_mappings.keys():
                digit = hex_mappings[digit]
        decimal_number += int(digit) * (base ** highest_digit_exp)
        highest_digit_exp -= 1

    return decimal_number

def factorial(number):
    # Top-down approach
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)