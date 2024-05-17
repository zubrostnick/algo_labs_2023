"""
https://www.eolymp.com/uk/submissions/13181794
"""


def binary_search(n, k, stalls):
    l = 1
    r = stalls[-1] - stalls[0] + 1

    while l < r:
        m = l + (r - l) // 2
        cow_counter = 1  # amount of cows we can fit according to current m value
        stall_index1 = 0
        stall_index2 = 1

        while stall_index2 < n:
            if stalls[stall_index2] - stalls[stall_index1] < m:
                stall_index2 += 1
            else:
                cow_counter += 1
                stall_index1 = stall_index2
                stall_index2 += 1

        if cow_counter >= k:
            l = m + 1  # m
        else:
            r = m

    return l - 1


if __name__ == "__main__":
    n, k = [int(s) for s in input().split()]
    stalls_coordinates = sorted(map(int, input().split()))
    print(binary_search(n, k, stalls_coordinates))
