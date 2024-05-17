# class Heap:
#     """Реалізація структури Купи за допомогою списку (макс)"""
#
#     def __init__(self):
#         # перший елемент фіктивний
#         # par = curr // 2
#         self.items = [None]
#
#     def insert(self, item):
#         self.items.append(item)
#         self.sift_up()
#
#     def swap(self, i, j):
#         self.items[j], self.items[i] = self.items[i], self.items[j]
#
#     def sift_up(self):
#         """Просіювання вверх"""
#         # просіюємо допоки в елемента є батько
#         curr = len(self.items) - 1
#         while curr > 1:
#             parent = curr // 2
#             if self.items[curr] < self.items[parent]:
#                 break
#             self.swap(curr, parent)
#             curr = parent
#
#     def sift_down(self):
#         curr = 1  # корінь
#         while curr * 2 < len(self.items):
#             left = curr * 2
#             right = left + 1
#             if right < len(self.items) and self.items[left] < self.items[right]:
#                 child = right
#             else:
#                 child = left
#             if self.items[child] < self.items[curr]:
#                 break
#             self.swap(child, curr)
#             curr = child
#
#     def extract_max(self):
#         if len(self.items) == 1:
#             return
#         self.swap(1, -1)
#         item = self.fitems.pop()
#         self.sift_down()
#
#
# def heapsort(array):
#     n = len(array)
#     # створення купи
#     for i in range((n - 1) // 2, -1, -1):
#         sift_down(array, i, n)
#     # сортування купи
#     for i in range(1, n):
#         # останній елемент не в массиві, а у купі
#         array[0], array[n - i] = array[n - i], array[0]
#         sift_down(array, 0, n - i)
#
#
# def sift_down(array, curr, end):
#     while True:
#         left = curr * 2 + 1  # бо починається з нуля, а не з 1
#         right = left + 1
#
#         largest = curr
#         if left < end and array[largest] < array[left]:
#             largest = left
#         if right < end and array[largest] < array[right]:
#             largest = right
#         if largest == curr:
#             break  # вже купа, зупиняємо роботу фукнції
#         array[curr], array[largest] = array[largest], array[curr]
#         curr = largest
#
#
# if __name__ == "__main__":
#     with open("input.txt") as f:
#         heap = Heap()
#         n = int(f.readline())
#         for _ in range(n):
#             command, *args = map(int, f.readline().split())
#             if command == 0:
#                 heap.insert(*args)
#             elif command == 1:
#                 heap.extract_max()




class Heap:
    """Реалізація структури Купи за допомогою списку (макс)"""

    def __init__(self):
        # перший елемент фіктивний
        # par = curr // 2
        self.items = [None]

    def ADD(self, id, priority):
        item = Node(id, priority)
        self.items.append(item)
        self.sift_up(len(self.items) - 1)

    def swap(self, i, j):
        self.items[j], self.items[i] = self.items[i], self.items[j]

    def sift_up(self, curr):
        """Просіювання вверх"""
        # просіюємо допоки в елемента є батько
        #curr = len(self.items) - 1
        while curr > 1:
            parent = curr // 2
            if self.items[curr].priority < self.items[parent].priority:
                break
            self.swap(curr, parent)
            curr = parent

    def sift_down(self, curr=1):
        """Просіювання вниз"""
        #curr = 1  # корінь
        while curr * 2 < len(self.items):
            left = curr * 2
            right = left + 1
            if right < len(self.items) and self.items[left].priority < self.items[right].priority:
                child = right
            else:
                child = left
            if self.items[child].priority < self.items[curr].priority:
                break
            self.swap(child, curr)
            curr = child

    def POP(self):
        if len(self.items) == 1:
            return
        self.swap(1, -1)
        item = self.items.pop()
        self.sift_down()
        print(item.id, item.priority)

    def CHANGE(self, id, new_priority):
        index = self.find_elem(id)
        self.items[index].priority = new_priority
        self.sift_up(index)
        self.sift_down(index)


    # def CHANGE(self, id, new_priority):
    #     for i in range(1, len(self.items)):
    #         if self.items[i].id == id:
    #             self.items[i].priority = new_priority
    #             if new_priority > self.items[i].priority:
    #                 self.sift_down(i)
    #             else:
    #                 self.sift_up(i)
    #             break

    def find_elem(self, id):
        for i in range(1, len(self.items)):
            if self.items[i].id == id:
                return i

    def execute(self, command):
        method, *args = command.split()
        getattr(self, method)(*args)



def heapsort(array):
    n = len(array)
    # створення купи
    for i in range((n - 1) // 2, -1, -1):
        sift_down(array, i, n)
    # сортування купи
    for i in range(1, n):
        # останній елемент не в массиві, а у купі
        array[0], array[n - i] = array[n - i], array[0]
        sift_down(array, 0, n - i)


def sift_down(array, curr, end):
    while True:
        left = curr * 2 + 1  # бо починається з нуля, а не з 1
        right = left + 1

        largest = curr
        if left < end and array[largest] < array[left]:
            largest = left
        if right < end and array[largest] < array[right]:
            largest = right
        if largest == curr:
            break  # вже купа, зупиняємо роботу фукнції
        array[curr], array[largest] = array[largest], array[curr]
        curr = largest


if __name__ == "__main__":
    with open("input.txt") as f:
        heap = Heap()
        for line in f:
            heap.execute(line)
            print(*[(elem.priority, elem.id) for elem in heap.items[1:]])
        #print(heap.items[heap.find("one")].priority)

