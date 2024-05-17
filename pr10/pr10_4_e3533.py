# Алгоритмом повного перебору
"""
https://www.eolymp.com/uk/submissions/13405521
"""


def find_min_time(missions, time, score):
    global min_time
    global K
    # print(missions, time, score)
    if time > min_time:
        return
    elif score >= K:
        min_time = time
        time

    for i in range(len(missions)):
        sub_missions = missions[i + 1:]  # missions[:i] + missions[i+1:]
        find_min_time(sub_missions, time + missions[i][1], score + missions[i][0])


if __name__ == "__main__":
    min_time = float("inf")
    N, K = map(int, input().split())
    missions = []
    for i in range(N):
        missions.append(tuple(map(int, input().split())))

    find_min_time(missions, 0, 0)
    print(min_time)
