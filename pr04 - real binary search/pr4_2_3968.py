"""
https://www.eolymp.com/uk/submissions/13157957
"""

from math import sqrt

def solve_eq(c):
    #Точність по аргументу
    eps = 1e-7
    l = 0.0
    r = 100000.0
    while (r - l) > eps:
        m = (r + l) / 2.0
        if m * m + sqrt(m) < c:
            l = m
        else:
            r = m
    return l


if __name__ == "__main__":
    inp = float(input())
    print("{:.9f}".format(solve_eq(inp)))
