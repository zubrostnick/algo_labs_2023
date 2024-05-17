"""
https://www.eolymp.com/uk/submissions/13149616
"""


def linear_search(array, l, r):
    counter = 0
    for player_height in array:
        if l <= player_height <= r:
            counter += 1
    return counter


if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.readline().strip()
        while line:
            n = int(line)
            array = list(map(int, f.readline().split()))
            a, b = [int(s) for s in f.readline().split()]
            print(linear_search(array, a, b))
            line = f.readline().strip()
