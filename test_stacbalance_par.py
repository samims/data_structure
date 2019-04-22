import unittest

from stack import Stack
from stack_balance_par import is_balanced


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.stack.items = ['A', 'B', 'C']

    def test_get_items(self):
        self.assertEqual(self.stack.get_stack(), ['A', 'B', 'C'])

    def test_push_item(self):
        self.stack.push('D')
        self.assertEqual(self.stack.get_stack(), ['A', 'B', 'C', 'D'])

    def test_check_top_item_after_push(self):
        self.stack.push('D')
        self.assertEqual(self.stack.items[-1], 'D')

    def test_pop(self):
        pop_item = self.stack.pop()
        self.assertEqual(pop_item, 'C')

    def test_stack_not_empty(self):
        empty = self.stack.is_empty()
        self.assertFalse(empty)

    def test_stack_is_empty(self):
        self.stack = Stack()
        self.assertTrue(self.stack.is_empty())


class TestParenBalance(unittest.TestCase):
    def test_paren_is_not_balanced(self):
        self.assertFalse(is_balanced('()[(())]]'))
        self.assertFalse(is_balanced('(]()'))

    def test_paren_is_balanced(self):
        self.assertTrue(is_balanced('[]()[[(())]]'))
