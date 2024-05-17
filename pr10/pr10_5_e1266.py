# Алгоритмом повного перебору
"""
https://www.eolymp.com/uk/submissions/13407872
"""


# def max_music_time(music, time):
#     global music_max
#     global N
#     global s
#     if time > N:
#         return
#     elif time > music_max:
#         music_max = time
#
#     for i in range(len(music)):
#         sub_music = music[i + 1:]  # missions[:i] + missions[i+1:]
#         max_music_time(sub_music, time + music[i])


def max_music_time(time, song_num):
    global music_max

    if music_max == N or time > N:
        return

    if song_num >= s:
        if music_max <= time <= N:
            music_max = time
        return

    # рекурсивний виклик без урахуванням місії mission_num
    max_music_time(time, song_num + 1)
    max_music_time(time + music[song_num], song_num + 1)




if __name__ == "__main__":
    with open("input.txt") as f:
        for line in f:
            music_max = 0
            inp = list(map(int, line.split()))
            N, s, music = inp[0], inp[1], inp[2:]
            #max_music_time(music, 0)
            max_music_time(0, 0)
            print("sum:", music_max, sep='')
