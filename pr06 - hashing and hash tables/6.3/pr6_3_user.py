"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

author_keys = []
books_values = []
size = 100007


def _hash(word):
    """ Метод згортки для рядків"""
    global size

    n = 29  # Просте число, що не перевищує 255
    h = 0
    for i in range(len(word)):
        h = h * n + ord(word[i])
    return h % size


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global author_keys, books_values, size
    author_keys = [None for _ in range(size)]
    books_values = [None for _ in range(size)]


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """

    curr = _hash(author)
    while author_keys[curr] is not None:
        if author_keys[curr] == author and books_values[curr] == title:
            return
        curr = (curr + 1) % size

    author_keys[curr] = author
    books_values[curr] = title


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    curr = _hash(author)
    while author_keys[curr] is not None:
        if author_keys[curr] == author and books_values[curr] == title:
            return True
        curr = (curr + 1) % size

    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """

    curr = _hash(author)
    items = []
    while author_keys[curr] is not None:
        if author_keys[curr] != author and books_values[curr] != title:
            items.append((author_keys[curr], books_values[curr]))

        author_keys[curr] = None
        books_values[curr] = None
        curr = (curr + 1) #% size

    for aut, book in items:
        addBook(aut, book)


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    result = []

    curr = _hash(author)
    while author_keys[curr] is not None:
        if author_keys[curr] == author:
            result.append(books_values[curr])
        curr = (curr + 1) #% size

    return sorted(result)


# if __name__ == "__main__":
