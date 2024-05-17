"""
https://www.eolymp.com/uk/submissions/13150109
"""


# Використайте бінарний пошук для знаходження відповіді для кожного вказаного інтервалу.

def find_one(array, x):
    left = 0
    right = len(array)
    while left < right:
        m = left + (right - left) // 2
        if array[m] < x:
            left = m + 1
        else:
            right = m

    if left != len(array):
        if array[left] == x:
            first = left
    else:
        return 0

    left = 0
    right = len(array)
    while left < right:
        m = left + (right - left) // 2
        if array[m] <= x:
            left = m + 1
        else:
            right = m

    if (array[left - 1]) == x:
        return left - first
    else:
        return 0


def find_many(main_array, search_array):
    for species in search_array:
        print(find_one(main_array, species))


if __name__ == "__main__":
    with open("input.txt") as f:
        f.readline()
        main_array = list(map(int, f.readline().split()))
        f.readline()
        search_array = list(map(int, f.readline().split()))
        find_many(main_array, search_array)
