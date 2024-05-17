"""
https://www.eolymp.com/uk/submissions/13149860
"""
# num_butterflies = 2 * 10 ** 9

def find_one(array, x):
    l = 0
    r = len(array)-1
    while l < r:
        m = l + (r - l) // 2
        if array[m] < x:
            l = m + 1
        else:
            r = m

    if (array[l]) == x:
        return 'YES'
    else:
        return 'NO'


def find_many(main_array, search_array):
    for type in search_array:
        print(find_one(main_array, type))


if __name__ == "__main__":
    with open("input.txt") as f:
        f.readline()
        main_array = list(map(int, f.readline().split()))
        f.readline()
        search_array = list(map(int, f.readline().split()))
        find_many(main_array, search_array)
