"""Discussion Questions
Given the tree above, in what order would a Breadth First Search (BFS)
algorithm visit each node until finding burritos (starting at food)? Just list
the order of nodes visited; no need to recreate the state of the algorithm data
in your answer.
Food, Italian, Indian, Mexican, lasagna, pizza, tikka masala, saag, burritos
Given the tree above, in what order would a Depth First Search (DFS) algorithm
visit each node until finding Chicago-style (starting at food)? Just list the
order of nodes visited; no need to recreate the state of the algorithm data in
your answer.
Food, Italian, lasagna, pizza, thin crust, chicago-style
How is a binary search tree different from other trees?
A binary search tree is a tree where each node has exactly two children (though
one or both children may be None), and the node data is arranged so that for any
node X, all nodes to the left of X have data less than X's data, and all nodes
to the right of X have data greater than X's data.  That means that if we are
searching for a node Y, we start at the top, and compare Y.data to our current
node's data, and depending on the result we either go left or right.  At each
level we eliminate half of the data, so searching is much faster.
"""

"""Tree class and tree node class."""


class Node(object):
    """Node in a tree."""

    def __init__(self, data, children=None):
        children = children or []
        assert isinstance(children, list), \
            "children must be a list!"
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node %s>" % self.data

    def get_num_children(self):
        """Get number of children.

        For example::

            >>> a = Node("A", [Node("B"), Node("C")])
            >>> a.get_num_children()
            2
        """

        # FIXME

        pass


class Tree(object):
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Tree root=%s>" % self.root

    def depth_first_search(self, data):
        """Return node object with this data, traversing the tree depth-first.

        Start at the root, and return None if not found.
        """

        to_visit = [self.root]

        while to_visit:
            node = to_visit.pop()

            if node.data == data:
                return node

            to_visit.extend(node.children)


    def breadth_first_search(self, data):
        """Return node object with this data, traversing the tree breadth-first.

        Start here (on this node), and return None if not found.

        Let's make a tree where we have two "B" nodes, but where one is far down an
        earlier branch and the other is higher-up in an earlier branch. Since this is
        a BFS, we should find the b2 node for "B"::

                       A
                     /   \
                    C     E
                   /       \
                  D        B2
                 /
                B1

            >>> a = Node("A")
            >>> b1 = Node("B")
            >>> b2 = Node("B")
            >>> c = Node("C")
            >>> d = Node("D")
            >>> e = Node("E")
            >>> a.children = [c, e]
            >>> c.children = [d]
            >>> d.children = [b1]
            >>> e.children = [b2]
            >>> tree = Tree(a)

            >>> tree.breadth_first_search("B") is b2
            True

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

