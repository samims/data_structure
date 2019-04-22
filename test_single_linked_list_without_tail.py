import unittest
from linked_list import Node, SingleLinkedList


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node = Node(data=5)

    def test_node_is_created(self):
        self.assertEqual(self.node.data, 5)
        self.assertEqual(self.node.next, None)


class TestSingleLinkedListWithoutTail(unittest.TestCase):
    def setUp(self):
        self.linked_list = SingleLinkedList()

    def test_head_is_none_by_default(self):
        self.assertIsNone(self.linked_list.head)

    def test_prepend_to_empty_list(self):
        node = Node(1)
        self.linked_list.prepend(node)
        self.assertEqual(self.linked_list.head.data, node.data)
        self.assertIsNone(self.linked_list.head.next)

    def test_prepend_to_non_empty_list(self):
        node1 = Node(1)
        node2 = Node(2)
        self.linked_list.prepend(node1)
        self.linked_list.prepend(node2)

        self.assertEqual(self.linked_list.head.data, node2.data)
        self.assertEqual(self.linked_list.head.next, node1)
        self.assertEqual(self.linked_list.head.next.data, node1.data)
        self.assertIsNone(self.linked_list.head.next.next)
