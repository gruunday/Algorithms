## CheatSheet for Algorithms 

### Contents
1. [Stacks](#Stacks)
2. [bla](#bla)

### Stacks

* Abstract Data Type (ADT)
  * Replaces data structures
  * It defines what the Data Type can do, not how it does it, or implemented

* Stack
  * Always add to the top
  * Always take off the top
  * Can be used to reverse sequence

* Stack ADT
  * isempty() # is stack empty
  * push()    # put an item on the stack
  * pop()     # removes the item from a stack

* Example of the stack

```python
stack = Stack()
for v in 'aeiou':
    stack.push(v)

while not stack.isempty():
    print(stack.pop())
```

* Applications
  * Browser History
  * Reverse Input
  * Matching Brackets

Operation | Big O Performance
------------ | -------------
isempyt() | Constant time
push() | Constant time
pop() | Constant time


### bla
