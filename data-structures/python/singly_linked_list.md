# Singly Linked Lists

-   Contains _head_, _tail_, and _length_ properties.
-   Consist of nodes, each _node_ has a _value_ and _pointer_ to another node or None.
    '

## Time Complexity:

-   Push: O(1)
-   Pop: O(n)
-   Shift: O(1)
-   Unshift: O(1)

## Singly Linked Lists vs Arrays

### Lists

-   Do not have indexes.
-   Connected via nodes with a _next_ pointer.
-   Random Access isn't allowed.

### Arrays

-   Indexed in order.
-   Insertion and deletion can be expensive.
-   Can quickly be accessed at a specific index.

##Singly Linked List methods

### Push (insert_at_tail)

#### Pseudocode

1. Create a new node with the value passed into the method as an argument upon invocation.
2. If the linked list that you are calling this method on has no head.
   2b. Make the head of the linked list the new node.
   2c. Make the tail of the linked list the new node.
3. Else
   3b. Make the next pointer of the linked list's tail point to the new node.
   3c. Make the tail of the linked list the new node.

#### Python implementation

```python

def push(self, value):
    new_node = node(value)
    if (self.head is None):
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node
        self.tail = new_node

    self.length += 1;
    return self.length;

```

### POP (remove_from_tail)

#### Pseudocode

1. Check if the linked list is not None, else don't do anything
2. Create variable current that points to the linked list's head
3. Create a variable new_tail that points to current
4. While current has a next node
   4b. set new_tail to current
   4c. set current to current.next
5. Set the tail of the linked list to new_tail
6. Set the next pointer of the linked lists tail to none.
7. Decrement the length of the linked list by one.

#### Python implementation

```python

def pop(self):
    if self.head is not None:
        current = self.head
        new_tail = current
        while current.next is not None:
            new_tail = current
            current = current.next
        self.tail = new_tail
        self.tail.next = None
        self.length -= 1
        return current
```

### UNSHIFT

#### Pseudocode

1. Create a new node with the value passed in as an argument to the method.
2. If the linked list has no head
   2a. Set the head of the linked list equal to the new node
   2b. Set the tail of the linked list equal to the new node
3. Else
   3a. set the next pointer of the new_node to the linked list's head
   3b. set the linked list's head to the new_node
4. Increment the length of the linked list by one.
5. Return the length of the linked list.
