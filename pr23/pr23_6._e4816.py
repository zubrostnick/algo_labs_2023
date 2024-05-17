from collections import deque
"""
https://www.eolymp.com/uk/submissions/13817019
"""

def bfs_compSv(ss, countNode):
    used = [False] * countNode
    compSv = [0] * countNode
    countCompSv = 0

    for i in range(countNode):
        if not used[i]:
            q = deque()
            q.append(i)
            used[i] = True
            countCompSv += 1

            while q:
                cur = q.popleft()
                compSv[cur] = countCompSv

                for child in ss[cur]:
                    if not used[child]:
                        used[child] = True
                        q.append(child)

    return compSv, countCompSv


if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        ss = [[] for _ in range(n)]

        for _ in range(m):
            a, b = map(int, f.readline().split())
            a -= 1
            b -= 1

            ss[a].append(b)
            ss[b].append(a)

    compSv, countCompSv = bfs_compSv(ss, n)

    mp = {}

    for i in range(n):
        if compSv[i] not in mp:
            mp[compSv[i]] = set()
        mp[compSv[i]].add(i)

    print(countCompSv)

    for d in mp.values():
        print(len(d))
        print(" ".join(str(k + 1) for k in d))
