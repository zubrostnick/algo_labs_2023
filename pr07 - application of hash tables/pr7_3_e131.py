import itertools
import math


##https://www.eolymp.com/uk/submissions/13363668


def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class Set:
    X = 13

    def __init__(self, word, size=10001):
        self._size = size
        self._count = 0
        self._keys = [None for _ in range(size)]

        for i in range(1, len(word) + 1):
            for v in itertools.permutations(word, i):
                self.add("".join(v))

    def hash(self, s):
        h = 0
        for c in s:
            h = h * self.X + ord(c)
        return h % self._size

    def _rehash(self):
        _size = self._size
        _keys = self._keys

        self._size = 2 * _size + 1
        while not is_prime(self._size):
            self._size += 2

        self.__init__(self._size)
        for key in _keys:
            if key:
                self.add(key)

    def add(self, key):
        if self._count > 0.7 * self._size:
            self._rehash()

        curr = self.hash(key)
        while self._keys[curr] is not None:
            if self._keys[curr] == key:
                return
            curr = (curr + 1) % self._size

        self._keys[curr] = key
        self._count += 1

    def find(self, key):
        curr = self.hash(key)
        while self._keys[curr] is not None:
            if self._keys[curr] == key:
                return True
            curr = (curr + 1) % self._size
        return False

    def keys(self):
        res = []
        for key in self._keys:
            if key is not None:
                res.append(key)
        return res


if __name__ == "__main__":
    words = Set(input())
    number = int(input())
    counter = 0
    for i in range(number):
        if words.find(input()):
            counter += 1
    print(counter)
