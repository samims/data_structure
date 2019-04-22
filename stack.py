class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False


s = Stack()
# s.push("A")
# s.push("B")
# print(s.get_stack())
#
# s.push("C")
# # s.pop()
# print(s.get_stack())
# s.pop()
# print(s.get_stack())
