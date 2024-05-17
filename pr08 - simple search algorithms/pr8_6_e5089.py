"""
https://www.eolymp.com/uk/submissions/13376108
"""


def selection_sort(array):  # lexicographic, ascending order
    arr_len = len(array)

    for i in range(arr_len - 1, 0, -1):
        maxpos = 0
        for j in range(1, i + 1):
            if array[maxpos] < array[j]:
                maxpos = j

        array[maxpos], array[i] = array[i], array[maxpos]


if __name__ == "__main__":
    n = int(input())
    array = []
    for i in range(n):
        array.append(input())

    selection_sort(array)
    print(*array, sep="\n")
