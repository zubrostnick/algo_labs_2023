#
# from map table import UnsortedTableMap
# class ChainHashMap (HashMapBase):
#     def _bucket_getitem(self , j, k):
#         bucket = self._table[j]
#         if bucket is None:
#             raise KeyError ('Key Error {0}'.format(k))
#         return bucket[k]
#
#     def _bucket_setitem(self, j, k, v):
#         if self._table [j] is None:
#             self._table [j] = UnsortedTableMap()
#         oldsize = len(self._table [j])
#         self._table [j][k] = v
#         if len(self._table [j]) > oldsize :
#             self._n += 1
#
#     def _bucket_delitem(self , j, k):
#         bucket = self._table[j]
#         if bucket is None:
#             raise KeyError ('Key Error {0}'.format(k))
#         del bucket [k]
#
#     def __iter__(self):
#         for bucket in self._table :
#             if bucket is not None:
#                 yield from bucket

#
#

#

class LinkedList:
    class _Node:
        def	__init__(self, element):
            self._element = element
            self._next_element = None

    def	__init__(self):
        self._head = None
        self._size = 0

    def add(self, element):
        node = self._Node(element)
        if not self._head:
            self._head = node
        else:
            current_node = self._head
            while current_node._next_element:
                current_node = current_node._next_element
            current_node._next_element = node
        self._size += 1

    def remove_first(self):
        if self._size == 0:
            raise Exception("List is empty")
        self._head = self._head._next
        self._size -= 1

    def __iter__(self):
        current = self._head
        while current:
            yield current._element
            current = current._next


lst = LinkedList()
#  add   values for value in lst:
for value in lst:
    print(value)# use value  for  something

