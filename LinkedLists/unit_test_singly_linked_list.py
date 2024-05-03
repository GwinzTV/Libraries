import unittest
import linkedlist as ll

'''
Unit tests to verify functionality of the linked list library
'''

class TestExamples(unittest.TestCase):
    def test_delete_data_from_list(self):
        # arrange
        sll = ll.SinglyLinkedList()
        for i in range(10):
            sll.append(i)
        sll.print_list()
        # act
        result = sll.delete(5)
        # assert
        self.assertEqual(result, 5)


    def test_prepend_data_to_list(self):
        # arrange
        sll = ll.SinglyLinkedList()
        for i in range(5):
            sll.append(i)
        sll.print_list()
        sll.prepend('99')
        # act
        result = sll.head.data
        # assert
        self.assertEqual(result, '99')


if __name__ == "__main__":
    unittest.main()