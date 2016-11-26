class Queue:

#
#   Queue Template
#

    # Initalise Queue
    def __init__(self, capacity = 4):
        self.data = [0] * capacity
        self.front = 0
        self.back = 0
    
    # Count the items in the queue
    def count(self):
        if self.back >= self.front:
            return self.back - self.front
        else:
            return self.back - self.front + len(self.data)
    
    # Check to see if the queue is empty
    def isempty(self):
        return self.front == self.back
    
    # Put something on the end of the queue
    def enqueue(self, item):
        if self.count() < len(self.data) - 1:
            self.data[self.back] = item
            self.back = (self.back + 1) % len(self.data)
        else:
            print("Queue Full")
    
    # Remove something from the front of the queue
    def dequeue(self):
        if self.count() > 0:
           item = self.data[self.front]
           self.front = (self.front + 1) % len(self.data)
           return item
        else:
            return None
