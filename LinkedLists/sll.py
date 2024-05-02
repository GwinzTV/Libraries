'''
This library seamlessly allows you to create singly linked lists!!!
I have made sure to make this library and its methods easy to understand by adding
comment where I can. I hope you find ease in its use!

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

# linked list class
class LinkedList:
    '''
    This linked list class contains a variety of standard list manipulation/interaction methods
    to suit your needs and make the idea of creating a linked list a simple reality!
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
        if self.head == None:
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
        if self.head == None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    