from math import sin

"""
4.4. На відрізку [1.6, 3] знайдіть корінь рівняння
sin 𝑥 = 𝑥 / 3.
"""

def solve_eq():
    #  безпосереднє сусідство двох дійсних чисел
    l = 1.6
    r = 3
    m = (l + r) / 2.0   
    while l != m and m != r:
        if m/3 - sin(m) < 0:
            l = m
        else:
            r = m
        m = (l + r) / 2.0
    return l


if __name__ == "__main__":
    print(solve_eq())  #  Відповідь: x0 = 2.279
