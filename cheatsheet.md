## CheatSheet for Algorithms 

### Contents
1. [SelectionSort](#SelectionSort)
1. [Stacks](#Stacks)
2. [Queues](#Queues)
3. [LinkedLists](#LinkedLists)

### SelectionSort
* In-place comparaison sort
* O(n**2) time complexity
* General case worse than insertion sort
* Noted for simplicity
* Good when auxillary memory is limited

* Example

```python
6, 12, 13, 7, 3, 10 # unordered list

3, 12, 13, 7, 6, 10 # swap 6, 3

3, 6, 13, 7, 12, 10 # swap 12, 6

3, 6, 7, 13, 12, 10 # swap 13, 7

3, 6, 7, 10, 12, 13 # swap 13, 10

3, 6, 7, 10, 12, 13 # now sorted
```

* Heapsort improves the algorithm by impelmenting an implicict heap data structure
* This speeds up finding and removing the lowest value
* The heap will aloow finding the next lowest element in O(logN) time instead of O(n)
* This makes it over all N(logN)

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


### Queues

* Queues
  * Similar to stack
  * Difference is first itm placed in queue will be the last removed
  * Items come off in the same order that they went on
  * First In First Out (FIFO)

* Queue ADT
  * isempty() # is the queue empty
  * enqueue() # put an item in the queue
  * dequeue() # removes item from the queue

* Example of the queue

```python
queue = Queue()
for v in 'aeiou':
    queue.enqueue(v)

while not queue.isempty():
    queue(queue.dequeue())
```

* Applications
  * The queue is often implemented as a circular list with two pointers
  * Front: where items are to be removed
  * Back: where items are to be added

Operation | Big O Performance
------------ | -------------
isempyt() | Constant time
enqueue() | Constant time
dequeue() | Constant time

### LinkedLists

* Linked Lists
  * A chain of Nodes
  * Stores series of elements
  * Each node has two parts. Item and pointer
  * Last pointer points to None
  * First Node is called the head

```python
class Node:
    def __init__(self, item, next):
        self.item = item
        self.item = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = None(item, self.head)

    def is_empty(self):
        return self.head == None
```

* Linked List ADT
  * isempty() # is linkedlist empty
  * add()     # add item to the list
  * remove()  # remove item from the list

```python
from LinkedList import LinkedList

ll = LinkedList()

for v in 'aeiou':
    ll.add(v)
```

