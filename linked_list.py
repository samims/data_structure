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

    def top_front(self):
        if self.head is None:
            return None

        return self.head

    def pop_front(self):
        if self.head is None:
            return None
        item = self.head
        self.head = self.head.next
        return item

    def top_back(self):
        if self.head is None:
            return None
        i = self.head
        while i.next is not None:
            i = i.next
        return i

    def pop_back(self):
        if self.head is None:
            return None
        if self.head.next is None:
            node = self.head
            self.head = None
            return node
        i = self.head
        while i.next.next is not None:
            i = i.next
        node = i.next
        i.next = None
        return node

    def find(self, key):
        if not self.head:
            return False
        cur_head = self.head
        while cur_head:
            if cur_head.data == key:
                return True
            cur_head = cur_head.next
        return False

    def remove(self, key):
        if not self.head:
            return
        cur_node = self.head
        prev_node = None
        while cur_node:
            if cur_node.data == key:
                if not prev_node:
                    self.head = None
                    return cur_node.data
                if cur_node.next:
                    prev_node.next = cur_node.next
                    return cur_node.data
                prev_node.next = None
                return cur_node
            cur_node = cur_node.next
        return None
