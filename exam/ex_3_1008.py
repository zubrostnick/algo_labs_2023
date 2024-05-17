"""
https://www.eolymp.com/uk/submissions/13889605
"""

def convert(number, base_from, base_to):
    dec_number = 0
    power = 0
    number = number[::-1]
    for digit in number.strip():
        dec_number += get_decimal_digit(digit) * (base_from ** power)
        power += 1

    stack = []
    while dec_number > 0:
        stack.append(dec_number % base_to)
        dec_number //= base_to
    converted = ""
    while stack:
        converted = converted + get_char_digit(stack.pop())
    return converted


def get_decimal_digit(digit):
    try:
        return int(digit)
    except:
        return ord(digit) - ord("A") + 10


def get_char_digit(digit):
    if digit <= 9:
        str_digit = str(digit)
    else:
        str_digit = chr(ord("A") + digit - 10)
    return str_digit


if __name__ == "__main__":
    with open("input.txt") as f:
        base_1, base_2 = map(int, f.readline().split())
        num = f.readline()

    print(convert(num, base_1, base_2))
