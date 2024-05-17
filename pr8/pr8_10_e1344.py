"""
https://www.eolymp.com/uk/submissions/13378256
"""


def insertion_sort(array):
    arr_len = len(array)
    for index in range(1, arr_len):
        current_val = array[index]
        position = index
        while position > 0:
            if array[position - 1] > current_val:
                array[position] = array[position - 1]  # зсув елементу вправо

            else:
                break  # якщо знайдено позицію
            position -= 1

        array[position] = current_val


if __name__ == "__main__":
    n = int(input())
    array = []
    for _ in range(n):
        sirname = input()
        name = input()
        grade_full = input()
        grade = (int(grade_full[0:-1]), grade_full[-1])
        # grade_let = grade_full[-1]
        birth = input()
        array.append((grade, sirname, name, birth))

    # print(array)

    insertion_sort(array)

    for doc in array:
        print(*doc[0], sep="", end=" ")
        print(*doc[1:])

    # print(array[0] < array[1])
