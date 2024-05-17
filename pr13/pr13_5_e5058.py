"""
https://www.eolymp.com/uk/submissions/13503873
"""


def parenthesis_check(seq: str):
    par_dict = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for par in seq:
        if par in par_dict.keys():
            stack.append(par)

        elif stack:
            if par_dict[stack.pop()] != par:
                print("no")  # false
                return
        else:
            print("no")  # False
            return

    print("yes" if len(stack) == 0 else "no")


if __name__ == "__main__":
    parenthesis_check(input())
