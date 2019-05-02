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
        self.node1 = Node(1)
        self.node2 = Node(2)
        self.node3 = Node(3)
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

    def test_pop_front_empty_linked_list(self):
        self.assertIsNone(self.linked_list.pop_front())

    def test_top_front(self):
        self.assertIsNone(self.linked_list.top_front())
        self.linked_list.prepend(self.node1)
        self.assertTrue(self.linked_list.top_front(), self.node1)

    def test_pop_front_non_empty_linked_list(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)

        self.linked_list.prepend(node1)
        self.linked_list.prepend(node2)
        self.linked_list.prepend(node3)

        self.assertTrue(self.linked_list.pop_front(), node3)
        self.assertTrue(self.linked_list.pop_front().data, node2.data)

    def test_top_back_empty_linked_list(self):
        self.assertIsNone(self.linked_list.top_back())

    def test_top_back_non_empty_linked_list(self):
        self.linked_list.prepend(self.node1)
        self.linked_list.prepend(self.node2)

        self.assertEqual(self.linked_list.top_back(), self.node1)

    def test_pop_back_empty_linked_list(self):
        self.assertIsNone(self.linked_list.pop_back())

    def test_pop_back_single_value_linked_list(self):
        self.linked_list.prepend(self.node1)
        self.assertEqual(self.linked_list.pop_back(), self.node1)

    def test_pop_back_multi_value_linked_list(self):
        self.linked_list.prepend(self.node1)
        self.linked_list.prepend(self.node2)
        node3 = Node(3)
        self.linked_list.prepend(node3)
        self.assertEqual(self.linked_list.pop_back(), self.node1)
        self.assertEqual(self.linked_list.pop_back(), self.node2)

    def test_find_key_in_empty_linked_list(self):
        self.assertFalse(self.linked_list.find(1))

    def test_find_key_in_non_empty_list(self):
        self.linked_list.prepend(self.node1)
        self.linked_list.prepend(self.node2)
        self.assertTrue(self.linked_list.find(1))

    def test_remove_blank_linked_list(self):
        self.assertIsNone(self.linked_list.remove(1))

    def test_remove_key_from_single_item_linked_list(self):
        # TODO check if linked list object changed
        # comp_linked_list = SingleLinkedList()
        self.linked_list.prepend(self.node1)
        self.assertEqual(self.linked_list.remove(1), 1)
        # self.assertIs(comp_linked_list, self.linked_list)

    def test_remove_key_from_two_items_linked_list(self):
        self.linked_list.prepend(self.node1)
        self.linked_list.prepend(self.node2)
        self.assertEqual(self.linked_list.remove(2), 2)

    def test_remove_key_from_multi_items_linked_list(self):
        self.linked_list.prepend(self.node1)
        self.linked_list.prepend(self.node2)
        self.linked_list.prepend(Node(3))
        self.assertEqual(self.linked_list.remove(2), 2)

    def test_is_empty(self):
        self.assertTrue(self.linked_list.is_empty())
        self.linked_list.prepend(self.node2)
        self.assertFalse(self.linked_list.is_empty())

    def test_insert_before_if_prev_node(self):
        self.linked_list.prepend(self.node1)
        self.linked_list.prepend(self.node2)
        self.linked_list.prepend(self.node3)
        self.linked_list.add_before(3, 4)

        self.assertTrue(self.linked_list.find(4))
        self.assertEqual(self.linked_list.add_before(3, 4), 4)

    def test_insert_before_if_prev_none(self):
        self.assertIsNone(self.linked_list.add_before(1, 1))
        self.linked_list.prepend(self.node1)
        self.linked_list.add_before(1, 1)

