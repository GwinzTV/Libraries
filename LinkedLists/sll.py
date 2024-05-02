'''
This library seamlessly allows you to create singlely linked lists!!!
I have made sure to make this library and its methods easy to understand by adding
comment where I can. I hope you find ease in its use!

        ==============================
        |==       DEVELOPER:       ==|
        |==    Joshua Iyinkanmi    ==|
        ==============================
'''

# node for building a singley linked list
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# linked list class
class LinkedList():
    def __init__(self):
        self.head = None

    # time complextity O(1)
    def add_node_beginning(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    # time complexity O(n)
    def add_node_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    