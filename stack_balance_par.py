from stack import Stack


def is_balanced(par_string):
    stack = Stack()

    for char in par_string:
        if char in '[(':
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            top = stack.pop()
            if (char == ')' and top != '(') or (char == ']' and top != '['):
                return False
    return stack.is_empty()