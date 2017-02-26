"""Discsusion Questions
Given the linked list below, which are the nodes? 
The boxes are the nodes - the box containing ("Apple" | next), the box
containing ("Berry" | next), the box containing ("Cherry" | next).

What is the data for each node?
The data for each node is the text string: "Apple", "Berry", "Cherry".
Where is the head?
The head is the node with data "Apple".
Where is the tail?
The tail is the node with data "Cherry".

What’s the difference between doubly- and singly-linked lists?
In a singly linked list, each node has an attribute to track the "next" node in
the list, but no attribute to track the "prev" node in the list.  In a doubly
linked list, each node has an attribute for both "next" and "prev", so that
we can traverse a doubly linked list in either direction.
Why is it faster to append to a linked list if we keep track of the tail as an
attribute?
Without tail as an attribute of the list, in order to find the end of the list,
we have to traverse the entire list until we find a node whose "next" is None.
This is an O(n) operation.  If we keep track of the tail of a linked list, then
finding the end of the list is O(1), because we don't need to traverse the list,
we can just check the tail.
"""
# Linked list with Node/LinkedList classes


class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node %s>" % self.data


class LinkedList(object):
    """Linked List using head and tail."""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        """Add node with data to end of list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    def remove_node_by_index(self, index):
        """Remove node with given index."""

        prev = None
        node = self.head
        i = 0

        while (node is not None) and (i < index):
            prev = node
            node = node.next
            i += 1

        if prev is None:
            self.head = node.next
        else:
            prev.next = node.next

    def find_node(self, data):
        """Is a matching node in the list?"""

        current = self.head

        while current is not None:
            if current.data == data:
                return True

            current = current.next

        return False

    def print_list(self):
        """Print all items in the list::

            >>> ll = LinkedList()
            >>> ll.add_node('dog')
            >>> ll.add_node('cat')
            >>> ll.add_node('fish')

            >>> ll.print_list()
            dog
            cat
            fish
        """

        # FIXME

        pass

    def get_node_by_index(self, idx):
        """Return a node with the given index::

            >>> ll = LinkedList()
            >>> ll.add_node('dog')
            >>> ll.add_node('cat')
            >>> ll.add_node('fish')

            >>> ll.get_node_by_index(0)
            <Node dog>

            >>> ll.get_node_by_index(2)
            <Node fish>
        """

        # FIXME

        pass

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

