# Option 1
# def lightweight(weight=0, plate_num=0):
#     global plates
#     if plate_num >= K:
#         return
#     lightweight(weight, plate_num + 1)
#     lightweight(weight + plates[plate_num], plate_num + 1)


# Option 2


# для прискорення функціонування функції lightweight (зменшення кількості рекурсивних викликів - повторень)
# Результат піднявся до 71, але все інше - помилки
plates_rem = []


# 21a
# def lightweight(plates, weight=0):
#     global plates_rem
#     #print(weight, plates_rem, plates)
#
#     #find_pair(plates, weight)   - 1
#     #find_pair(plates_rem, weight)  #2a
#     find_pair(weight, len(plates_rem)) #2b
#
#     #print(weight, plate_num)
#
#     for i in range(len(plates)):
#         weight_next = weight + plates[i]          #sub_plates = plates[i + 1:]  # missions[:i] + missions[i+1:]
#         # А що якщо оця перевірка паскудить? Просто перенести окремо для виклику find_pair.
#         # Там теж таке є, тож нащо повторюватись
#         # if weight_next not in result:  - 71 - 73. Чітко. А що тоді?
#
#         # Problem might be here:changing from plates plates[i + 1:] to plates[:i] + plates[i + 1:]
#         # Maybe we can return back numbers_rem, so to simplify lightweight() and fix find_pair()
#         # lightweight(plates[:i] + plates[i + 1:], weight_next)   # Було 67 стало 54 (помилки->time limits extension)
#         plates_rem = plates[:i] + plates[i + 1:]
#         lightweight(plates[i + 1:], weight_next)  # 2a
#

# 21b


# Ідея: переробити фукнцію find_pair так, щоб plates_rem залишався правильним (не враховуються елементи, які були взяті попередньо )
# Спробувати ввести partial = [] - список, що містить використані елементи.
# Або plates remaining як параметр.

def lightweight(plates, used=[]):
    global plates_rem, full_plates

    plates_rem = full_plates[:]
    for elem in used:
        plates_rem.remove(elem)

    find_pair(sum(used), len(plates_rem))  # 2b

    # print(weight, plate_num)

    for i in range(len(plates)):
        # sub_plates = plates[i + 1:]  # missions[:i] + missions[i+1:]
        # plates_rem = plates[:i] + plates[i + 1:]
        lightweight(plates[i + 1:], used + [plates[i]])  # 2a


# 2a
# def find_pair(numbers, goal_num, partial=[]):
#     global result
#     s = sum(partial)
#
#     if s > goal_num or goal_num in result:
#         return  # if we reach the number why bother to continue
#
#
#     # check if the partial sum is equals to target
#     if s == goal_num:
#         result.append(s)
#         #print("sum({})={}".format(partial, goal_num))
#         return
#
#     for i in range(len(numbers)):
#         n = numbers[i]
#         remaining = numbers[i + 1:]
#         find_pair(remaining, goal_num, partial + [n])

# 2b
def find_pair(goal_num, amount, curr_sum=0, curr_num=0):
    global result, plates_rem
    # print(goal_num, plates_rem,curr_sum, curr_num)

    if goal_num in result or curr_sum > goal_num:
        return

    # check if the partial sum is equals to target
    if curr_sum == goal_num:
        result.append(curr_sum)
        # print("sum({})={}".format(partial, goal_num))
        # print("Adding", curr_sum)
        return

    if curr_num >= amount:
        return  # if we reach the number why bother to continue

    # рекурсивний виклик без урахуванням місії mission_num
    find_pair(goal_num, amount, curr_sum, curr_num + 1)
    find_pair(goal_num, amount, curr_sum + plates_rem[curr_num], curr_num + 1)  # how to get numbers? - add plates_rem


#  C. Poblem: index in num array excludes possible options. Might be a problem with the first one

# numbers_rem = []

# def lightweight(plates, weight=0):
#     ##
#     global numbers_rem
#     ##
#     find_pair(plates, weight)
#
#     #print(weight, plate_num)
#
#     for i in range(len(plates)):
#         weight_next = weight + plates[i]          #sub_plates = plates[i + 1:]  # missions[:i] + missions[i+1:]
#         if weight_next not in result:
#             #lightweight(plates[i + 1:], weight_next)
#
#             numbers_rem = plates[i + 1:]
#             lightweight(weight_next, len())
#


# def find_pair(goal_num, amount, curr_sum=0, curr_num=0):
#     global result, numbers_rem
#
#     if goal_num in result or curr_sum > goal_num or curr_num >= amount:
#         return  # if we reach the number why bother to continue
#
#     # check if the partial sum is equals to target
#     if curr_sum == goal_num:
#         result.append(goal_num)
#         #print("sum({})={}".format(partial, goal_num))
#         return
#
#
#
#     # рекурсивний виклик без урахуванням місії mission_num
#     find_pair(goal_num, amount, curr_sum, curr_num + 1)
#     find_pair(goal_num, amount, curr_sum + numbers_rem[curr_num],  curr_num + 1)  #how to get numbers?


if __name__ == "__main__":
    N, K = map(int, input().split())
    barbells = list(map(int, input().split()))
    plates = list(map(int, input().split()))
    plates_rem = plates[:]  # 2b

    full_plates = plates[:]
    combinations = []
    # lightweight()
    # for barbell in barbells:
    result = []
    lightweight(plates)

    final_result = []
    for barbell in barbells:
        for res in result:
            sum = barbell + res * 2
            if sum not in final_result:
                final_result.append(sum)

    print(*sorted(final_result), sep='\n')
