"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

library_items = []
size = 100007


class Node:

    def __init__(self, author, book):
        self.author = author
        self.book = book
        self.next = None


def _hash(word):
    """ Метод згортки для рядків"""
    global size

    n = 31  # Просте число, що не перевищує 255
    h = 0
    for i in range(len(word)):
        h = h * n + ord(word[i])
    return h % size


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global library_items, size
    library_items = [None for _ in range(size)]


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    curr = _hash(author)
    node = library_items[curr]
    while node is not None:
        if node.author == author and node.book == title:
            return
        node = node.next

    node = Node(author, title)
    node.next = library_items[curr]
    library_items[curr] = node


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    curr = _hash(author)
    node = library_items[curr]
    while node is not None:
        if node.author == author and node.book == title:
            return True
        node = node.next
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    curr = _hash(author)
    node = library_items[curr]
    if node is not None:
        if node.author == author and node.book == title:
            library_items[curr] = node.next
            return

        prev = node
        node = node.next
        while node is not None:
            if node.author == author and node.book == title:
                prev.next = node.next
                return

            prev = node
            node = node.next


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    result = []
    curr = _hash(author)
    node = library_items[curr]
    while node is not None:
        if node.author == author:
            result.append(node.book)
        node = node.next

    return sorted(result)
