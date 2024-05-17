"""
https://www.eolymp.com/uk/submissions/13503644
"""


def convert(number, to_base):

    stack = []
    while number > 0:
        stack.append(number % to_base)
        number //= to_base

    result = ""
    while stack:
        result += get_char(stack.pop())
    return result


def get_char(d: int):
    if d < 10:
        return str(d)
    else:
        return "[" + str(d) + "]"


if __name__ == "__main__":
    num = int(input())
    base = int(input())
    print(convert(num, base))
