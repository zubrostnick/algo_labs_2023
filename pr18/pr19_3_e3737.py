"""
https://www.eolymp.com/uk/submissions/13679799
"""


def check_heap(array):
    n = len(array)
    for i in range(1, (n - 1) // 2 + 1):
        if 2 * i < n and array[i] > array[2 * i]:
            return "NO"
        if 2 * i + 1 < n and array[i] > array[2 * i + 1]:
            return "NO"

    return "YES"


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        arr = [None] + list(map(int, f.readline().split()))

    print(check_heap(arr))
