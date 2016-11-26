class Stack:

#
#  Stack Template
#
    
    # Initalise the stack 
    def __init__(self):
        self.stack = []
        self.top = 0

    
    # Check to see if the stack is empty
    def is_empty(self):
        return self.top == 0
    
    
    # Pushes item onto the stack
    def push(self, item):
        if self.top < len(self.stack):
            self.stack[self.top] = item
        else:
            self.stack.append(item)

        self.top += 1
    
    
    # Pops the top item off the stack
    def pop(self):
        if self.is_empty():
            return None
        else:
            self.top -= 1
            return self.stack[self.top]
