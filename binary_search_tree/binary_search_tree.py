"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.insert(0, value)

    def dequeue(self):
        if len(self.storage) == 0:
            return
        return self.storage.pop(-1)

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #no root
        if self.value is None:
            self.value = value

        # < root
        if self.value > value:
            # already a value
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

        # >= root
        if self.value <= value:
            # already a value
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        found = False
        if self.value >= target:
            if self.left is None:
                return False
            found = self.left.contains(target)

        if self.value < target:
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value

        # Why do I need to return the function?
        return self.right.get_max()

        
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call on root
        fn(self.value)

        #call on both sides if not none
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        #if left is not none:
            #call on left child
        if self.left is not None:
            self.left.in_order_print(self.left)

        #print value
        print(node.value)

        #if right is not none:
            #call on right child
        if self.right is not None:
            self.right.in_order_print(self.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = []
        queue.append(self)

        while len(queue) != 0:
            node = queue.pop(0)
            print(node.value)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(self)

        while len(stack) != 0:
            node = stack[-1]
            stack.pop()
            print(node.value)

            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node is not None:
            #print value
            print(node.value)

            #if left is not none:
            #call on left child
            if self.left is not None:
                self.left.pre_order_dft(self.left)

            #if right is not none:
                #call on right child
            if self.right is not None:
                self.right.pre_order_dft(self.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is not None:
            #if left is not none:
            #call on left child
            if self.left is not None:
                self.left.post_order_dft(self.left)

            #if right is not none:
                #call on right child
            if self.right is not None:
                self.right.post_order_dft(self.right)

            #print value
            print(node.value)



bst = BSTNode(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.post_order_dft(bst)