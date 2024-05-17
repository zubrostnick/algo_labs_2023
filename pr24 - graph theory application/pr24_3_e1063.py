"""
https://www.eolymp.com/uk/submissions/13817231
"""


from collections import deque

runx = [0, 1, 0, -1]
runy = [1, 0, -1, 0]


def bfs(a, b):
    global used

    q = deque()
    used[a][b] = True
    q.append((a, b))

    while q:
        cur = q.popleft()
        i, j = cur

        for k in range(4):
            ii = i + runx[k]
            jj = j + runy[k]

            if 0 <= ii < n and 0 <= jj < m and not used[ii][jj] and v[ii][jj] == '#':
                used[ii][jj] = True
                q.append((ii, jj))


def solve(n, m):
    global used
    res = 0

    for i in range(n):
        for j in range(m):
            if v[i][j] == '#' and not used[i][j]:
                res += 1
                bfs(i, j)

    return res


if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        v = [list(f.readline().strip()) for _ in range(n)]
    used = [[False] * m for _ in range(n)]

    print(solve(n, m))
