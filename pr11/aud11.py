# max_income: int = 0
#
#
# def solve(vouchers, income, day):
#     global max_income
#     print(vouchers, income, day)
#     if len(vouchers) == 0 and income > max_income:
#         max_income = income
#
#     for i in range(len(vouchers)):
#         sub_income = income + vouchers[i][1] * (vouchers[i][0] - day)
#         sub_vouchers = [] # тільки актуальні путівки
#         for j in range(len(vouchers)):
#             if i != j and vouchers[j][0] - day > 1:
#                 sub_vouchers.append(vouchers[j])
#
#         solve(sub_vouchers, sub_income, day + 1)
#
#
# if __name__ == "__main__":
#     with open("input.txt") as f:
#         n = int(f.readline())
#         vouchers = []
#         for _ in range(n):
#             d, c = map(int, f.readline().split())
#             vouchers.append((d, c))
#
#         solve(vouchers, 0, 0)
#         print(max_income)
#

DRAW = 0
FIRST = 1
SECOND = 2   # черговість гравців

size = 0
OO = "0"
XX = "X"


def play(field: str, turn):
    print(field, turn)

    i = -1
    while True:   #Шукаємо пустий блок клітинок, куди гравець може зробити хід
        i = field.find(OO, i + 1)
        if i == -1:
            break
        sub_field = field[:i] + XX + field[i + size:]
        sub_turn = SECOND if turn == FIRST else FIRST
        #play(sub_field, sub_turn)
        # якщо даний хід нам поверне перемогу даного гравця, то він повинен його зробити
        if play(sub_field, sub_turn) == turn:
            return turn

    return SECOND if turn == FIRST else FIRST  # якщо будь-який крок приводить до поразки


if __name__ == "__main__":
    with open("input.txt") as f:
        n, k = map(int, f.readline().split())  # n - поле, к - розмір блоку
        string = f.readline().strip()

        size = k
        OO *= size
        XX *= size

        if string.find(OO) == -1:  # шукаємо у рядку блок, куди можна зробити хід
            print(DRAW)
        else:
            print(play(string, FIRST))





