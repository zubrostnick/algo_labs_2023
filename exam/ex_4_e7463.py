"""
https://www.eolymp.com/uk/submissions/13889326
"""


class SearchTree:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        node = self
        while True:
            if key < node.key:
                if node.left is None:
                    node.left = SearchTree(key)
                    break
                else:
                    node = node.left
            elif key >= node.key:
                if node.right is None:
                    node.right = SearchTree(key)
                    break
                else:
                    node = node.right
            else:
                break

    def max_depth(self):
        left_depth = 0 if self.left is None else self.left.max_depth()
        right_depth = 0 if self.right is None else self.right.max_depth()
        return max(left_depth, right_depth) + 1


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        keys = list(map(int, f.readline().split()))

        tree = SearchTree(keys[0])
        for key in keys[1:]:
            tree.insert(key)

    print(tree.max_depth())



