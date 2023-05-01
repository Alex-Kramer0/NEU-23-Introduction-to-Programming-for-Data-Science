'''
Alex Kramer
DS 5010
Spring 2023
Homework 4
'''

# SOURCES: used to learn more, and correct some of my own code / make things work in less lines
# https://realpython.com/python-deque/#:~:text=They%20work%20as%20a%20pipe,favorite%20restaurant%20as%20an%20example
# https://www.educative.io/answers/how-to-use-a-deque-in-python
# https://www.geeksforgeeks.org/deque-in-python/
# https://medium.com/@kevin.michael.horan/data-structures-linked-lists-with-python-2d0ec4fdc18c

class Node:
    """
    A class for a node in a doubly-linked list, storing
    a data payload and links to next and previous nodes.
    """

    def __init__(self, data = None, prev = None, next = None):
        """Initialize the node with data payload and link to next node."""
        self.data = data
        self.next = next
        self.prev = prev

    def getdata(self):
        """Get the node's data payload."""
        return self.data

    def setdata(self, data = None):
        """Set the node's data payload."""
        self.data = data

    def getnext(self):
        """Get the next linked node."""
        return self.next

    def setnext(self, node = None):
        """Set the next linked node."""
        self.next = node

    def getprev(self):
        """Get the previous linked node."""
        return self.prev

    def setprev(self, node = None):
        """Set the previous linked node."""
        self.prev = node

class Deque:
    """
    A double-ended queue supporting accessing
    the items at either end of the container.
    """

    def __init__(self):
        """Initializes an empty deque storing both head and tail nodes."""
        self.head = None
        self.tail = None
        self.size = None

    def __iter__(self):
        """Returns a forward iterator over the deque."""
        node = self.head
        while node is not None:
            yield node.getdata()
            node = node.getnext()

    def __reversed__(self):
        """Returns a reverse iterator over the deque."""
        node = self.tail
        while node is not None:
            yield node.getdata()
            node = node.getprev()

    def __str__(self):
        """Returns a string representation of the deque."""
        return " -> ".join([str(x) for x in self])

    def __repr__(self):
        """Returns a printable representation of the deque."""
        return str(self)

    def __len__(self):
        """Returns the length of the deque."""
        size = 0
        for i in self:
            size += 1
        self.size = size
        # save size as a new attribute
        return size

    ### Problem 1

    def push(self, data):
        """
        Adds a new item to the front of the deque.
        param data: The new item to prepend to the deque.
        returns: None
        """

        new_node = Node(data)
        if self.head is None:
            # if que is empty, create new head and tail
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        size = self.__len__()
        self.size += 1
        # updates que size

    ### Problem 2

    def pop(self):
        """
        Removes and returns the front item of the deque.
        returns: The item removed from the front deque, or None if empty.
        """
        if self.head is None:
            return None
            # if que is empty return None
        else:
            value = self.head.getdata
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            size = self.__len__()
            self.size += 1
            # updates que size
            return value

    def peek(self):
        """
        Returns the front item of the deque (without removing it).
        returns: The item at the front of the deque, or None if empty.
        """
        if self.head is not None:
            return self.head.getdata()

    ### Problem 3

    def push_back(self, data):
        """
        Adds a new item to the back of the deque.
        param data: The new item to append to the deque.
        returns: None
        """
        new_node = Node(data)
        if self.tail is None:
            # if que is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        size = self.__len__()
        self.size += 1
        # updates que size

    ### Problem 4

    def pop_back(self):
        """
        Removes and returns the item at the back of the deque.
        returns: The item removed from the back of the deque, or None if empty.
        """
        if self.tail is None:
            return None
            # if que is empty
        else:
            value = self.tail.getdata
            self.tail = self.tail
            if self.tail is not None:
                self.tail.next = None
            else:
                self.head = None
            size = self.__len__()
            self.size -= 1
            return value
            # updates size

    def peek_back(self):
        """
        Returns the item at the back of the deque (without removing it).
        returns: The item at the back of the deque, or None if empty.
        """
        if self.tail is not None:
            return self.tail.getdata()

    ### Problem 5

    def find(self, value):
        """
        Finds the index of the given value in the deque.
        param value: The value to search for in the deque.
        returns: The index of the value if it exists; otherwise, None.
        """
        index = 0
        # index acts as our counter for where we are
        node = self.head
        while node is not None:
            if node.getdata == value:
                return index
            node = node.next
        index += 1
        return index


if __name__ == "__main__":
    x = Deque()
    x.push("1!")
    x.push("2!")
    x.push("3!")
    print(x)  # 3! -> 2! -> 1!
    x.pop()  # 3!
    print(x)  # 2! -> 1!
    x.push_back("go!")
    print(x)  # 2! -> 1! -> go!
    x.pop_back()  # go!
    x.pop()  # 2!
    x.pop()  # 1!
    x.pop()  # None
    print(x)
    y = Deque()
    y.push_back(1.11)
    y.push_back(2.22)
    y.push_back(3.33)
    print(y)  # 1.11 -> 2.22 -> 3.33
    y.find(1.11)  # 0
    y.find(2.22)  # 1
    y.find("a")  # None
    print(y.find(2.22))