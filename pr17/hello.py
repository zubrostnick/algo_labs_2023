class SearchTree:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        # є два варіанти: рекурсивний та нерекурсивний

        if key < self.key:
            if self.left is None:
                self.left = SearchTree(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = SearchTree(key)
            else:
                self.right.insert(key)

    def height(self):
        left_height = 0 if self.left is None else self.left.height()
        right_height = 0 if self.right is None else self.right.height()
        return (left_height, right_height) + 1

    def second_maximum(self):
        parent = None
        node = self
        # максимально по правому йдемо
        while node.right is not None:
            parent = node
            node = node.right

        if node.left is None:
            return parent.key

        node = node.left # лівий син максимального
        while node.right is not None:
            node = node.right

        return node.key


    def max_leaf(self):
        # пошук в ширину не підходить, бо будуть проблеми з сортуванням
        # використовуємо пошук в глибину
        result = []
        stack = [self]
        while stack:
            node = stack.pop()
            if node.left is None and node.right is None:
                result.append(node.key)

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:   # бо зі стеку виймається верхній елемент
                stack.append(node.left)

        return result


    def print(self):
        #пошук у глибину
        #print(self.key, end=' ')
        if self.left is not None:
            self.left.print()

        print(self.key, end=' ') # якщо тут поставити, то виведення буде у відсортованому  (момент виходу)
        if self.right is not None:
            self.right.print()



