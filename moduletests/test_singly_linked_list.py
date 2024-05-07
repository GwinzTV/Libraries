'''
unit test
'''

import unittest
from Libraries.linkedLists.ll import SinglyLinkedList


# Unit tests to verify functionality of the linked list library


class TestExamples(unittest.TestCase):
    '''
    unit testing for LinkedLists module
    '''
    def test_delete_data_from_list(self):
        '''
        test for delete method
        '''
        # arrange
        sll = SinglyLinkedList()
        for i in range(10):
            sll.append(i)
        # act
        result = sll.delete(5)
        # assert
        self.assertEqual(result, 5)


    def test_prepend_data_to_list(self):
        '''
        test for prepend method
        '''
        # arrange
        sll = SinglyLinkedList()
        for i in range(5):
            sll.append(i)
        sll.prepend('99')
        # act
        result = sll.head.data
        # assert
        self.assertEqual(result, '99')


if __name__ == "__main__":
    unittest.main()
