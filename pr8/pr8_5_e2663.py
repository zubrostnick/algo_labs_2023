"""
https://www.eolymp.com/uk/submissions/13375883
"""


def bubble_sort(array):
    arr_len = len(array)
    counter = 0
    for pass_num in range(arr_len - 1, 0, -1):
        _sorted = True
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                counter += 1
                _sorted = False
        if _sorted:
            return counter
    return counter


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))  # [4, 3, 2, 1]
    print(bubble_sort(array))
