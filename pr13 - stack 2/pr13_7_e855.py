"""
https://www.eolymp.com/uk/submissions/13504212
"""
# cтек + повний перебір

par_dict = {"(": ")", "[": "]"}   # "{": "}"}
all_parenthesis = list(par_dict.keys()) + list(par_dict.values())
result = []

def parenthesis_check(n, stack=[], res=''):
    global result

    if n == 0:
        if len(stack) == 0:
            result.append(res)
        return

    for par in all_parenthesis:
        if par in par_dict.keys():
            parenthesis_check(n - 1, stack + [par], res + par)
        elif stack:
            prev_par = stack.pop()
            if par_dict[prev_par] == par:
                parenthesis_check(n - 1, stack, res + par)
            stack.append(prev_par)


if __name__ == "__main__":
    parenthesis_check(int(input()))
    print(*result, sep='\n')
