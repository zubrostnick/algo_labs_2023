"""
https://www.eolymp.com/uk/submissions/13382463
"""


def merge_sort(array):
    if len(array) <= 1: return

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    merge_sort(left)
    merge_sort(right)

    i = k = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


if __name__ == "__main__":
    n = int(input())
    array = []
    for i in range(n):
        a, b = map(int, input().split())
        array.append(((a, i), b))
    merge_sort(array)

    for i in range(n):
        print(array[i][0][0], array[i][1])
