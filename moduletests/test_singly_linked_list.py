'''
unit testing
'''

import unittest
from linkedLists.ll import SinglyLinkedList


# Unit tests to verify the functionality of the linked list library


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        # ArrangeAll (to avoid clunky repeats)
        self.sll = SinglyLinkedList()
        for i in range(5):
            self.sll.append(i)

    def test_prepend_data_to_list(self):
        '''
        test for prepend method
        '''
        # arrange
        ll = self.sll
        ll.prepend('99')
        # act
        result = ll.head.data
        # assert
        self.assertEqual(result, '99')

    def test_append_method(self):
        '''
        test for append method
        '''
        # Arrange
        ll = self.sll
        # Act
        ll.append(99)
        last = ll.head
        while last.next is not None:
            last = last.next
        result = last.data
        # Assert
        self.assertEqual(result, 99)

    def test_delete_method(self):
        '''
        test for delete method
        '''
        # Arrange
        ll = self.sll
        # Act
        result = ll.delete(3)
        # Assert
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
