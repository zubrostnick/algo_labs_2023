"""
4.5. На відрізку [0, 2] знайдіть корінь рівняння
𝑥^3 + 4 𝑥^2 + 𝑥 − 6 = 0.
"""

def foo(x):
    return x ** 3 + 4 * x ** 2 + x - 6


def solve_eq(f, a, b, c):
    #  безпосереднє сусідство двох дійсних чисел
    l = a
    r = b
    m = (l + r) / 2.0
    while l != m and m != r:
        if f(m) < c:
            l = m
        else:
            r = m
        m = (l + r) / 2.0
    return l


if __name__ == "__main__":
    print(solve_eq(foo, 0, 2, 0))  #  Відповідь: x0 = 1
