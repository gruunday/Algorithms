## CheatSheet for Algorithms 

### Contents
1. [SelectionSort](#selectionsort)
2. [InsertionSort](#insertionsort)
3. [Stacks](#stacks)
4. [Queues](#queues)
5. [LinkedLists](#linkedlists)
6. [BinaryTree](#binarytree)
6. [AVLTree](#avltree)

### SelectionSort
* In-place comparaison sort
* O(n**2) time complexity
* General case worse than insertion sort
* Noted for simplicity
* Good when auxillary memory is limited

* Example

```python
[6, 12, 13, 7, 3, 10] # unordered list

[3, 12, 13, 7, 6, 10] # swap 6, 3

[3, 6, 13, 7, 12, 10] # swap 12, 6

[3, 6, 7, 13, 12, 10] # swap 13, 7

[3, 6, 7, 10, 12, 13] # swap 13, 10

[3, 6, 7, 10, 12, 13] # now sorted
```

* Heapsort improves the algorithm by impelmenting an implicict heap data structure
* This speeds up finding and removing the lowest value
* The heap will aloow finding the next lowest element in O(logN) time instead of O(n)
* This makes it over all N(logN)

### InsertionSort
* Simple sort algorithm that builds a sorted array one item at a time
* Not very efficient algorithm
* Advantages 
  * Simple implementation
  * Efficient for small data sets
  * More efficient in practice than other O(n**2) algorithms e.g selection sort
  * Efficient for sets that are already mostly sorted
  * Stable i.e does not change the relative order of elements with equal keys
  * In-place so it does not require any more memory

* Example

```python
[6, 12, 13, 7, 3, 10] # unordered list

[|6|, 12, 13, 7, 3, 10] # Assume that 6 is a sorted list of one item

[|6, 12|, 13, 7, 3, 10] # The 12 will stay to the right of the 6: 6 < 12

[|6, 12, 13|, 7, 3, 10] # All 3 elements are now sorted

[|6, 7, 12, 13|, 3, 10] # The 7 is moved to its correct place and all the other elements are moved up

[|3, 6, 7, 12, 13|, 10] # The 3 is moved to the start of the list

[|3, 6, 7, 10, 12, 13|] # The 10 is moved to its correct postion and the list is not sorted
``` 
* Best case for insertion sort is that they are all in order
* This then means that insertion sort has a linear run time O(n)

* Worset case is an array in reverse order
* This will give a result of O(n**2)

* Average case is also quadratic O(n**2)
* Impractical for sorting large arrays

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
isempty() | Constant time
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
  * delete()  # delete a particular item
  * count()   # number of items in the linked list
  * contains(item) # checks if the linked list contains the item

```python
from LinkedList import LinkedList

ll = LinkedList()

for v in 'aeiou':
    ll.add(v)
```
* Printing every element

  1. Start at the head
  2. If None we're Done, else print the item
  3. Repeat step 2 til Done

```python
ptr = head
while ptr != None:
    print(item)
    ptr = ptr.next
```

* Python List vs Linked List

Python List | Linked List
------------ | -------------
Constant time access based on idex. Nth element is O(n) | Constant time delete and insert operations
Many operations have constant time improvement| n\a 
Typically uses less memory | n\a 

* Can make it more useful by supporting builtins
  * __str__()
  * __len__()
  * __iter__()
  * __in__()

* Linked Lists go great with recursion
* Generally requires two functions. One to set up and then one to recurse

* Linked List Applications
  * Linked Lists can be easily used to impelement a stack or a queue
  * Advantage 
    * Never have to worry about it being full
    * Stack: Natural for a LinkedList

* Stack Example
```python
import LinkedList
class Stack:
    def __init__(self):
        self.linkedlist = LinkedList.LinkedList()
    
    def push(self, item):
        self.linkedlist.add(item)
    
    def pop(self):
        return self.linkedlist.remove()
    
    def is_empty(self):
        return self.linkedlist.is_empty()
```

* Queue
  * We need a pointer for the head and the tail
  * We add at the head and remove from the tail

* Queue Example
```python
import LinkedList
class Queue:
    def __init__(self):
        self.linkedlist = LinkedList.LinkedList()
    
    def enqueue(self, item):
        self.linkedlist.addlast(item)
 
    def dequeue(self):
        return self.linkedlist.remove()
 
    def is_empty(self):
        return self.linkedlist.is_empty()

    def addlast(self, item):
        if self.is_empty():
            self.tail = Node(item, None)
            self.head = self.tail
        else:
            self.tail.next = Node(item, None)
            self.tail = self.tail.next
```

### BinaryTree

* Binary tree
  * A binary tree is a collection of nodes.
  * Each node has a left and right pointer
  * A root node inicates the start of the tree. The roor is None for an empty tree

  * A Binary Search Tree (BST) is an implimentaion of a tree where:
    * All the values on the left of a node are smaller than the node itself
    * And all the values of the right of a node are larger than itself

  * It must be possible in a Binary Tree to compare values
  * Binary Tree can be used to implement a set
    * It may be possible that the same set has many layouts
  * Binary Tree can also be user to impelment a map (Dictionary)
    * You can store a value in addition to a key

* Tree Terminology

Name | Description
---------|----------------------------
Root | Top node in a tree
Child | A node directly spouting from a node above it
Parent | The opposite of the child node
Siblings | A group of child nodes with the same parent
Descendant | A node reachable through parent to child
Ancestor | A node reachable throught child to parent
Leaf / External Node | A node with no children
Internal Node | A node with a child
Edge | The connection between nodes
Path | A sequence of ndoes and edges connecting a node with a descendent
Height of a node | The height of a node is the number of edges on the longest path between that node and a leaf
Height of a tree | the height of a tree is the height of its root node

* The Node has an iten and left + right pointers
* The BST has a contains and an add method
* They are both of time complexity O(h)

* If you are using recursion with trees, you usually need two methods
  * One sets up for recursion
  * The other does the recusion

```python
def r_contains(self, ptr, item):
    # Recursice contains here

def constains(self, item):
    return self.r_contains(self.root, item)

```

* Height of a tree
  * The height of a tree is the maximum number of nodes from the root to a leaf.
  * The solution sould be recursive
  * If your left child had 2 children and your right child had 4 children you would have a height of 4

* Count the number of elements
  * If you were a leaf node you would have no children
  * If your left child had a subtree with 10 elements and your right child had a subtreee with 6 elements, you would have 16 elements

* Height and Balance
  * Many tree related operations are O(h) where h is the height of the tree
  * For a given number of elements, n, we would like to reduce the height of the tree
  * The best we can achieve is log(n) when the tree is balanced. The is when the difference in depth of any two leaves is at most 1

* Tree Traversal
  * This is how we get around to every element of the tree in some sort of order
  * These orders can be:
    * inorder
    * preorder
    * postorder
    * Useful link  https://en.wikipedia.org/wiki/Tree_traversal
  * This can be done recursively
  * The defference between pre and postis the order of the left and right instruction
  ```python
  def in_order(slef,ptr):
    if ptr != None:
        self.in_order(ptr.left)
        print(ptr.item)
        self.in_order(ptr.right)
  ```

* Tree Applications 
  * A set
    * It is the fastest way to check whether an item is in the set or not.
    * The add method needs to not add a duplicate
  * A map
    * The Node needs to store a value in addition to the key (item)
    * The add method should overwirt the value when a duplicate is added

### AVLTrees

* Problems with a BST
  * An unbalanced Binary Search Tree
  * A skewed BST has perforemaace similar to linked list
  * We want to keep the tree balanced by keeping the height at O(logN)

* An AVL Tree
  * This is a BST where the height is maintained O(logN)
  * This is done by adjusting the tree whenever it start to beome unbalanced
  * The add and delete operations may need to restucture the tree to maintain balance
  * We will only consider the add operation

* AVL Balance
  * We define a node to be AVL balanced when the difference in height between the two child nodes is less than or equal to one
  * Now, after we add a node, if the tree is no AVl balanced, we restrucutre it so that it is.
  * There are four cases when the tre becomes imbalanced
    * right-right
    * left-left
    * right-left
    * left-right
  * In each case we fix it by replacing the root with the middle element

* AVL Adding an element
  * Add the node to the tree
  * Start at this node, move up the tree towards the root checking to see if any node is now unbalanced.
  * If it is, find out which case itis and perform the correspinding restructuring.
  * Do this every time an element is added
  * It seems like a lot of work, but is is only O(logN)
  * No more than one restructuring is required per insert

* Search and add are now O(logN) operations because the height is O(logN)
