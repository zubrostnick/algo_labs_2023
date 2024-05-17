"""
https://www.eolymp.com/uk/submissions/13504559
"""

def par_shifts(seq):
    result = 0
    long_string = seq * 2
    for i in range(len(seq)):
        result += int(parenthesis_check(long_string[i:i+len(seq)]))

    return result



def parenthesis_check(seq: str):
    #par_dict = {"(": ")"} # "[": "]", "{": "}"}
    stack = []
    for par in seq:
        if par == "(":
            stack.append(par)

        elif stack:
            if par != ")":
                return False
            stack.pop()
        else:
            return False

    return len(stack) == 0


if __name__ == "__main__":
    print(par_shifts(input()))
