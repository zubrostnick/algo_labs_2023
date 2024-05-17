"""
https://www.eolymp.com/uk/submissions/13817359
"""
from collections import deque


def solve(n, v):
    ms = [
        ['O' for _ in range(n + 2)] for __ in range(n + 2)
    ]
    start, finish = None, None

    used = [
        [True for _ in range(n + 2)] for __ in range(n + 2)
    ]

    for i in range(n + 2):
        for j in range(n + 2):
            ch = ''
            border = i == 0 or i == n + 1 or j == 0 or j == n + 1
            if border:
                ms[i][j] = 'O'
            else:
                ch = v[i-1][j-1]
                ms[i][j] = ch

                if ch == '@':
                    start = (i, j)
                elif ch == 'X':
                    finish = (i, j)
                if ch != 'O':
                    used[i][j] = False

    qu = deque()
    qu.append(start)
    stack = []

    runx = [0, 1, 0, -1]
    runy = [1, 0, -1, 0]
    success = False

    while qu and not success:
        cur = qu.popleft()
        i, j = cur

        for k in range(4):
            ii = i + runx[k]
            jj = j + runy[k]

            if 0 <= ii < n+2 and 0 <= jj < n + 2 and not used[ii][jj]:
                used[ii][jj] = True
                qu.append((ii, jj))
                stack.append((cur, (ii, jj)))

                if (ii, jj) == finish:
                    success = True
                    break

    if not success:
        print("N")
        exit()

    cur = finish
    ms[cur[0]][cur[1]] = '+'

    while stack:
        top = stack.pop()

        if top[1] == cur and top[0] != start:
            ms[top[0][0]][top[0][1]] = '+'
            cur = top[0]

    print("Y")

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(ms[i][j], end='')
        print()


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        v = [list(f.readline().strip()) for _ in range(n)]

    solve(n, v)
