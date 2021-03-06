"""DISCUSSION QUESTIONS
1. In the following cases, would a stack or queue be a more appropriate data
structure?
The process of loading and unloading pallets onto a flatbed truck
Stack
Putting bottle caps on bottles of beer as they roll down an assembly line
Queue
Calculating the solution to this mathematical expression: 2 + (7 * 4) - (3 / 2)
Stack
2. Describe two more situations where a queue would be an appropriate data
structure.
The Hackbright help queue
Ikea instruction manual
The line for coffee
3. Describe two more situations where a stack would be an appropriate data
structure.
Pancakes!
Checking if an expression has matched parentheses
Undo in a computer program

"""

class StackEmptyError(IndexError):
    """Attempt to pop an empty stack."""


class Stack(object):
    """LIFO stack.

    Implemented using a Python list; since stacks just need
    to pop and push, a list is a good implementation, as
    these are O(1) for native Python lists. However, in cases
    where performance really matters, it might be best to
    use a Python list directly, as it avoids the overhead
    of a custom class.

    Or, for even better performance (& typically smaller
    memory footprint), you can use the `collections.deque`
    object, which can act like a stack.

    (We could also write our own LinkedList class for a
    stack, where we push things onto the head and pop things
    off the head (effectively reversing it), but that would be less
    efficient than using a built-in Python list or a
    `collections.deque` object)
    """

    def __init__(self):
        self._list = []

    def __repr__(self):
        if not self._list:
            return "<Stack (empty)>"
        else:
            return "<Stack tail=%s length=%d>" % (
                self._list[-1], len(self._list))

    def push(self, item):
        """Add item to end of stack."""

        self._list.append(item)

    def pop(self):
        """Remove item from end of stack and return it."""

        if not self._list:
            raise StackEmptyError()

        return self._list.pop()

    def __iter__(self):
        """Allow iteration over list.

        __iter__ is a special method that, when defined,
        allows you to loop over a list, so you can say things
        like "for item in my_stack", and it will pop
        successive items off.
        """

        while True:
            try:
                yield self.pop()
            except StackEmptyError:
                raise StopIteration

    def length(self):
        """Return length of stack::

            >>> s = Stack()
            >>> s.length()
            0

            >>> s.push("dog")
            >>> s.push("cat")
            >>> s.push("fish")

            >>> s.length()
            3
        """

        # FIXME

        return len(self._list)
        
    def empty(self):
        """Empty stack::

            >>> s = Stack()
            >>> s.push("dog")
            >>> s.push("cat")
            >>> s.push("fish")

            >>> s.length()
            3

            >>> s.empty()

            >>> s.length()
            0
        """

        # FIXME

        while self._list:
            self.pop()

    def is_empty(self):
        """Is stack empty?

            >>> s = Stack()

            >>> s.is_empty()
            True

            >>> s.push("dog")
            >>> s.push("cat")
            >>> s.push("fish")

            >>> s.is_empty()
            False
        """

        # FIXME

        if self.length():
            return False

        return True

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

