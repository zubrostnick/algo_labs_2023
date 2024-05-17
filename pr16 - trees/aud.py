# class PrefixTree:
#
#     def __init__(self):
#         self.children = {}
#
#     def add_child(self, digit):
#         self.children[digit] = PrefixTree()
#
#     def has_child(self, digit):
#         return digit in self.children
#
#     def get_child(self, digit):
#         return self.children[digit]
#
#     def is_leaf(self):
#         return not bool(self.children) # якщо словник пустий
#
#     def add_phone(self, phone: str):
#         node = self  # початок ланцюга
#         i = 0
#         while i < len(phone) and node.has_child(phone[i]):
#             node = node.get_child(phone[i]) # перехід на більш глибокий рівень
#             i += 1
#
#         if i == len(phone):
#             # якщо номер не сумісний (спільний початок)
#             return False
#
#         if i > 0 and node.is_leaf():
#             return False
#
#         while i < len(phone):
#             node.add_child(phone[i])
#             node = node.get_child(phone[i])
#             i += 1
#
# if __name__ == "__main__":
#     with open("input.txt") as f:
#         t = int(f.readline())
#         for _ in range(t):
#             tree = PrefixTree()
#             n = int(f.readline())
#             for __ in range(n):
#                 phone_number = f.readline().strip()
#                 if result: # якщо попередній був сумісний
#                     result = tree.add_phone(phone_number)
#
#             print("YES" if result else "NO")
#
from collections import deque


class Tree:

    def __init__(self, key, parent=None):
        self.key = key
        self.children = []
        self.parent = parent

    def dfs(self, key): # пошук в глибину
        if self.key == key:
            return self

        for child in self.children:
            node = child.dfs(key)
            if node is not None:
                return node


    def dfs_stack(self, key):
        stack = [self]
        while stack: # заглиблюємося та повертаємося назад
            node = stack.pop()
            if node.key == key:
                return node
            for child in node.children:
                stack.append(child)

    def bfs(self, key):
        queue = deque()
        queue.append(self)
        while queue:
            node = queue.popleft()  # забираємо зліва, додаємо зправа
            if node.key == key:
                print(type(node))
                return node
            for child in node.children:
                queue.append(child)


    def add(self, parent_key, key):
        parent = self.dfs(parent_key) # пошук батьківського
        node = Tree(key, parent)
        parent.children.append(node)

    def get(self, a, b):
        # алгоритм для знаходження першої вершини
        node = self.dfs(a)
        while node is not None:
            # пошук відносно конкретного вузла, а не цілого дерева
            if node.dfs(b) is not None:
                return node.key
            node = node.parent

    def execute(self, command):
        method, *args = command.split()
        method = method.lower()
        args = map(int, args)
        return getattr(self, method)(*args)


if __name__ == "__main__":
    with open("input.txt") as f:
        tree = Tree(1)
        k = int(f.readline())
        for _ in range(k):
            line = f.readline()
            result = tree.execute(line)
            if result is not None:
                print(result)
            for __ in range(n):
                phone_number = f.readline().strip()
                if result: # якщо попередній був сумісний
                    result = tree.add_phone(phone_number)

            print("YES" if result else "NO")

