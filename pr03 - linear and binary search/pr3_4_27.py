"""
https://www.eolymp.com/uk/submissions/13149420
"""


def test(n):
    shifted_digits = [int(x) for x in bin(n)[2::]]
    length = len(shifted_digits)
    result = 0
    for i in range(length):
        s = 0

        for j in range(length):
            s += shifted_digits[length - 1 - j] * 2**j

        if s > result: result = s

        shifted_digits.append(shifted_digits.pop(0))
    return result


if __name__ == "__main__":
    n = int(input())
    print(test(n))

