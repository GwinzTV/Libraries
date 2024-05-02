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
        self.__length_list = 0

    # getter for the length of the linked list
    def get_length_list(self):
        return self.__length_list
    
    # setter for length of linked list
    def set_length_list(self, increment=None):
        '''
        This method sets the value of the length of the linked list.
        '''
        if increment:
            self.__length_list += 1
            return
        if self.__length_list > 0:
            self.__length_list -= 1

    # time complextity O(1)
    def prepend(self, data):
        '''
        This method adds a new node to the beginning of the linked list.
        If there is no node at the beginning of the list, then the new node
        will become the first node in the list.
        '''
        new_node = Node(data)
        self.set_length_list(1)
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
        self.set_length_list(1)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    # time complexity O(n)
    def delete(self, data=None):
        '''
        This method deletes your chosen node, and if no node is specified,
        by default it will delete the last node in the list.
        '''
        current = self.head
        self.set_length_list()
        length = self.get_length_list()
        prev = None
        # no data specified, so delete last node
        if data == None:
            while current and current.next:
                prev = current
                current = current.next
            if length > 1:
                prev.next = None
            else:
                self.head = None
                print('Linked List is empty!')
            return
        # when data is specified
        while current.next.data != data:
            current = current.next
        current.next = current.next.next
    
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
    

    def search(self, index):
        '''
        This method takes an input index value and returns
        the data stored at that "index" in the linked list.
        '''
        current = self.head
        pass



# # manual testing
# ll = SinglyLinkedList()
# print(ll.get_length_list())
# for i in range(2):
#     ll.append(i)
# print(ll.get_length_list())
# ll.print_list()
# ll.delete()
# print(ll.get_length_list())
# ll.print_list()
# ll.delete()
# print(ll.get_length_list())
# ll.print_list()






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