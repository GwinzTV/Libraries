'''
This library seamlessly allows you to create singly linked lists!!!
I have made sure to make this library and its methods easy to understand by adding
comments and descriptive notes where I can. I hope you find ease in its use!

        ==============================
        |==       DEVELOPER:       ==|
        |==    Joshua Iyinkanmi    ==|
        ==============================
'''

# private node for building a singly linked list
class _Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# singly linked list class
class SinglyLinkedList:
    '''
    This linked list class contains a variety of standard list manipulation/querying methods
    to suit your needs and make the idea of creating a singly linked list a simple reality!
    '''
    def __init__(self):
        self.head = None
        self._length_list = 0

    # getter for the length of the linked list
    def get_length_list(self):
        return self._length_list
    
    # setter for length of linked list
    def set_length_list(self, increment=None):
        '''
        This method sets the value of the length of the linked list.
        '''
        if increment:
            self._length_list += 1
            return
        if self._length_list > 0:
            self._length_list -= 1

    # time complextity O(1)
    def prepend(self, data):
        '''
        This method adds a new _node to the beginning of the linked list.
        If there is no _node at the beginning of the list, then the new _node
        will become the first _node in the list.
        '''
        new__node = _Node(data)
        self.set_length_list(1)
        if not self.head:
            self.head = new__node
            return
        new__node.next = self.head
        self.head = new__node

    # time complexity O(n)
    def append(self, data, index = None):
        '''
        This method adds a _node to the end of the  linked list.
        If there is no _node in the list, then the new _node will become
        the first _node in the list.
        '''
        new__node = _Node(data)
        self.set_length_list(1)
        if not self.head:
            self.head = new__node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new__node
    
    # time complexity O(n)
    def delete(self, data):
        '''
        This method deletes your chosen _node from the list.
        '''
        current = self.head
        self.set_length_list()
        if current and current.data == data:
            self.head = current.next
            deleted = current.data
            current = None
            return deleted
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current != None:
            prev.next = current.next
            deleted = current.data
            current = None
            return deleted
        print(f'{data} is not in the linked list!')
    
    # time complexity O(n)
    def print_list(self):
        '''
        This method prints out the entire linked list
        (stretch goal: add slicing functionality)
        '''
        current = self.head
        if current:
            linked_list = ''
            while current:
                linked_list += str(current.data) + ' --> '
                current = current.next
            print(linked_list[0:-5])
        else:
            print('Linked list is empty!')
    
    # time complexity O(n)
    def search(self, value):
        '''
        This method takes an input value and returns
        the index that the data is stored in the linked list.
        '''
        current = self.head
        if current:
            index = 0
            if current.data == value:
                return f'{value} is found at index: {index}'
            while current and current.data != value:
                current = current.next
                index += 1
            if current:
                return f'{value} is found at index: {index}'
            return f'{value} is not in the list!'







# doubly linked list class
class DoublyLinkedList:
    '''
    This linked list class contains a variety of standard list manipulation/querying methods
    to suit your needs and make the idea of creating a doubly linked list a simple reality!
    '''
    # COMING SOON!
    pass


        
#         ========================================================
#         |==     I hope this Library has served you well!     ==|
#         |==      Please Leave feedback for improvements      ==|
#         |==    Your feedback will will help me improve on    ==|
#         |==                future projects.                  ==|
#         |==                                                  ==|
#         |==          Why not check out my Github:            ==|
#         |==           https://github.com/GwinzTV             ==|
#         |==                                                  ==|
#         ========================================================