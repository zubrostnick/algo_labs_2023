"""
https://www.eolymp.com/uk/submissions/13381711
"""


def quick_sort(array):
    _quick_sort(array, 0, len(array) - 1)


def _quick_sort(array, index_l, index_r):
    if index_l >= index_r: return

    pivot = array[index_l + (index_r - index_l) // 2]
    left = index_l
    right = index_r
    while True:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1

        if left >= right: break

        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    _quick_sort(array, index_l, right)  # could be left
    _quick_sort(array, right + 1, index_r)


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    quick_sort(array)
    print(*array)
