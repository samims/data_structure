"""
Operations to perform

PushFront(Key) -->  add to front

Key TopFront() -->  return front item

PopFront() -->  remove and return front item

PushBack(Key) -->  add to back  or Append

Key TopBack() -->  return back item

PopBack() -->  remove and return Back item

Boolean Find(Key) --> is key in list?

Erase(Key) --> remove key from list

Boolean Empty() --> empty list?

AddBefore(Node, Key) --> adds key before node

AddAfter(Node, Key) --> adds key after node

"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList(object):
    def __init__(self):
        self.head = None

    def prepend(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def top(self):
        if self.head is None:
            return None

        return self.head

    def pop_front(self):
        if self.head is None:
            return None
        item = self.head
        self.head = self.head.next
        return item
