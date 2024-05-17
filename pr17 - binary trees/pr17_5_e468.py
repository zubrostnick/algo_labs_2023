"""
https://www.eolymp.com/en/submissions/13662989
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
            elif key > node.key:
                if node.right is None:
                    node.right = SearchTree(key)
                    break
                else:
                    node = node.right
            else:
                break

    def print(self):
        if self.left is not None:
            self.left.print()
        print(self.key, end=" ")
        if self.right is not None:
            self.right.print()


def check_search_tree(seq):
    last = seq[-1]

    for i in range(len(seq) - 2):
        if not (seq[i] < last and seq[i] < seq[i+1] or seq[i] > last and seq[i] > seq[i+1]):
            return 'NO'
    return 'YES'


if __name__ == "__main__":
    with open("input.txt") as f:

        keys = list(map(int, f.readline().split()))

        tree = SearchTree(keys[0])
        for i in range(1, len(keys)):
            tree.insert(keys[i])

        print(check_search_tree(keys))

