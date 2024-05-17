"""
https://www.eolymp.com/uk/submissions/13889675
"""

def right_search(array, x):
    if x not in array:
        return 0
    left = 0
    right = len(array)
    while left < right:
        m = left + (right - left) // 2
        if array[m] <= x:
            left = m + 1
        else:
            right = m
    return left


if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        arr = list(map(int, f.readline().split()))

        for i in range(m):
            print(right_search(arr, int(f.readline())))
