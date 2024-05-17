"""
https://www.eolymp.com/uk/submissions/13424875
"""


# Your local gym has n barbells and m plates. In order to prepare a weight for lifting, you must choose a single barbell
# which has two sides. You then load each side with a (possibly empty) set of plates. For safety reasons, the plates
# on each side must sum to the same weight. What weights are available for lifting?

# For example, suppose that there are two barbells weighing 100 and 110 grams, and five plates weighting
# 1, 4, 5, 5 and 6 grams, respectively. Then, there are six possible weights available forlifting.
# The table below shows one way to attain the different weights:


def lightweight(plates, used=[]):
    global plates_rem, full_plates

    plates_rem = full_plates[:]  # Unused plates
    for elem in used:
        plates_rem.remove(elem)

    find_pair(sum(used), len(plates_rem))

    for i in range(len(plates)):
        # для прискорення функціонування функції lightweight (зменшення кількості рекурсивних викликів - повторень)
        lightweight(plates[i + 1:], used + [plates[i]])


def find_pair(goal_num, amount, curr_sum=0, curr_num=0):
    global result
    # print(goal_num, plates_rem,curr_sum, curr_num)

    if goal_num in result or curr_sum > goal_num:
        return

    if curr_sum == goal_num:
        result.append(curr_sum)
        return

    if curr_num >= amount:  # if we reach the number why bother to continue
        return

    # recursive call without considering curr_num
    find_pair(goal_num, amount, curr_sum, curr_num + 1)
    find_pair(goal_num, amount, curr_sum + plates_rem[curr_num], curr_num + 1)  # how to get numbers? - add plates_rem


if __name__ == "__main__":
    N, K = map(int, input().split())
    barbells = list(map(int, input().split()))
    full_plates = list(map(int, input().split()))
    plates_rem = full_plates[:]

    result = []
    lightweight(full_plates)

    final_result = []
    for barbell in barbells:
        for res in result:
            s = barbell + res * 2
            if s not in final_result:
                final_result.append(s)

    print(result)
    print(*sorted(final_result), sep='\n')
