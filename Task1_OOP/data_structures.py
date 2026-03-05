"""
data_structures.py - Custom Data Structures for the Library System
COMP8090SEF - Task 1 OOP Application: Library Management System
Student: HE Xue (SID: 13927408)

This module implements custom data structures used in the library system:
- LinkedList: For storing borrow history records
- Stack: For undo operations
- Queue: For reservation/waitlist management

Demonstrates:
- Encapsulation (private node structure)
- Composition (Node objects inside LinkedList)
- Iterator protocol (__iter__, __next__)
- Operator overloading (__len__, __contains__, __getitem__)
"""


class _Node:
    """
    Internal node class for LinkedList (encapsulated - private by convention).
    Each node stores data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    """
    Singly Linked List implementation.
    Used to store borrow history records in the library system.

    Demonstrates:
    - Composition (_Node objects inside LinkedList)
    - Iterator protocol (__iter__)
    - Magic methods (__len__, __contains__, __getitem__, __str__)
    """

    def __init__(self):
        self.__head = None   # Private: head of the list
        self.__size = 0      # Private: number of elements

    def append(self, data):
        """Add an element to the end of the linked list."""
        new_node = _Node(data)
        if self.__head is None:
            self.__head = new_node
        else:
            current = self.__head
            while current.next:
                current = current.next
            current.next = new_node
        self.__size += 1

    def prepend(self, data):
        """Add an element to the beginning of the linked list."""
        new_node = _Node(data)
        new_node.next = self.__head
        self.__head = new_node
        self.__size += 1

    def remove(self, data):
        """Remove the first occurrence of data from the list."""
        if self.__head is None:
            return False
        if self.__head.data == data:
            self.__head = self.__head.next
            self.__size -= 1
            return True
        current = self.__head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.__size -= 1
                return True
            current = current.next
        return False

    def to_list(self):
        """Convert linked list to a Python list."""
        result = []
        current = self.__head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def is_empty(self):
        """Check if the list is empty."""
        return self.__size == 0

    # --- Magic Methods ---

    def __len__(self):
        """Return the number of elements (supports len())."""
        return self.__size

    def __contains__(self, data):
        """Support 'in' operator."""
        current = self.__head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def __getitem__(self, index):
        """Support indexing with [] operator."""
        if index < 0:
            index = self.__size + index
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of range")
        current = self.__head
        for _ in range(index):
            current = current.next
        return current.data

    def __iter__(self):
        """Support iteration (for loop)."""
        current = self.__head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        """String representation of the linked list."""
        elements = []
        current = self.__head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "(empty)"


class Stack:
    """
    Stack implementation (LIFO - Last In, First Out).
    Used for undo/redo operations in the library system.

    Demonstrates:
    - Encapsulation (private internal list)
    - Magic methods (__len__, __str__, __bool__)
    """

    def __init__(self):
        self.__items = []  # Private internal storage

    def push(self, item):
        """Push an item onto the top of the stack."""
        self.__items.append(item)

    def pop(self):
        """Remove and return the top item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.__items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.__items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.__items) == 0

    # --- Magic Methods ---

    def __len__(self):
        return len(self.__items)

    def __str__(self):
        if not self.__items:
            return "Stack: (empty)"
        return "Stack (top -> bottom): " + " | ".join(
            str(item) for item in reversed(self.__items)
        )

    def __bool__(self):
        """Support truthiness check: bool(stack)."""
        return not self.is_empty()


class Queue:
    """
    Queue implementation (FIFO - First In, First Out).
    Used for reservation/waitlist management in the library system.

    Demonstrates:
    - Encapsulation
    - Magic methods (__len__, __str__, __bool__, __iter__)
    """

    def __init__(self):
        self.__items = []  # Private internal storage

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.__items.append(item)

    def dequeue(self):
        """Remove and return the front item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.__items.pop(0)

    def front(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.__items[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.__items) == 0

    # --- Magic Methods ---

    def __len__(self):
        return len(self.__items)

    def __str__(self):
        if not self.__items:
            return "Queue: (empty)"
        return "Queue (front -> back): " + " <- ".join(str(item) for item in self.__items)

    def __bool__(self):
        return not self.is_empty()

    def __iter__(self):
        """Support iteration over queue elements."""
        return iter(self.__items)

    def __contains__(self, item):
        """Support 'in' operator."""
        return item in self.__items
