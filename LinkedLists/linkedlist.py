'''
This library seamlessly allows you to create singly linked lists!!!
I have made sure to make this library and its methods easy to understand by adding
comments and descriptive notes where I can. I hope you find ease in its use!

        ==============================
        |==       DEVELOPER:       ==|
        |==    Joshua Iyinkanmi    ==|
        ==============================
'''

# node for building a singly linked list
class Node:
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

    # time complextity O(1)
    def prepend(self, data):
        '''
        This method adds a new node to the beginning of the linked list.
        If there is no node at the beginning of the list, then the new node
        will become the first node in the list.
        '''
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    # time complexity O(n)
    def append(self, data):
        '''
        This method adds a node to the end of the  linked list.
        If there is no node in the list, then the new node will become
        the first node in the list.
        '''
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    

    def delete(self, data=None):
        '''
        This method deletes your chosen node, and if no node is specified,
        by default it will delete the last node in the list.
        '''
        current = self.head
        # no data specified, so delete last node
        if data == None:
            while current.next.next:
                current = current.next
            current.next = None
            return
        # when data is specified
        while current.next.data != data:
            current = current.next
        current.next = None
    

    def print_list(self):
        '''
        This method prints out the entire linked list
        (stretch goal: add slicing functionality)
        '''
        pass



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