class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"(Node: value: {self.value} next: {self.next})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        return f"Head: {self.head} \nTail: {self.tail}\n Length: {self.length}\n"

    # PUSH
    def push(self, value):
        new_node = Node(value)
        if(self.head is None):
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self.length

    # POP
    def pop(self):
        if (self.head is not None):
            current = self.head
            new_tail = current
            while current.next is not None:
                new_tail = current
                current = current.next
            self.tail = new_tail
            self.tail.next = None
            self.length -= 1
            return current

    # SHIFT
    def shift(self):
        # If the linked list is not empty
        if (self.head is not None):
            # crreate a variable current_head and set it to the linked list's head
            current_head = self.head
            # set the head of the linked list to current_heads next pointer
            self.head = current_head.next
            # decrement the length by 1
            self.length -= 1
            # return current_head
            return current_head

    # UNSHIFT
    def unshift(self, value):
        new_node = Node(value)
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self.length


singly = SinglyLinkedList()


singly.push(1)
print("PUSH  \n", singly)
singly.push(2)
print("PUSH \n", singly)
singly.pop()
print("POP \n", singly)
singly.unshift(3)
print("UNSHIFT \n", singly)
singly.shift()
print("SHIFT \n", singly)
