from math import isqrt

a = 11
def is_square(number):
    return isqrt(number)**2 == number

for i in range(1000):
    a += 35
    if is_square(a):
        print(a)
        break
