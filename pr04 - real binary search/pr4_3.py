"""
4.3. Знайдіть найменше 𝑥∈[0, 10], що
𝑓(𝑥) = 𝑥^3 + 𝑥 + 1 > 5.

"""

def foo(x):
    return x ** 3 + x + 1


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
    print(solve_eq(foo, 0, 10, 5))  #  Відповідь: 1.379
