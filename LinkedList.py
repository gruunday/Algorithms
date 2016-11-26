#
#  Class to store item and next pointer
#

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

#
#  Linked List Template
#

class LinkedList:
    def __init__(self):
        self.head = None

    # adds item to the front of list
    def add(self, item):
        self.head = Node(item, self.head)

    # Removes item from 
    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove works by just moving the pointer to the next item
            return item

    # Check to see if the linked list is empty
    def is_empty(self):
        return self.head == None
