"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        self.length += 1
        new_node = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.length == 0:
            return None
        if self.length == 1:
            curr_head = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return curr_head.value
        elif self.length > 1:
            curr_head = self.head
            ListNode.delete(self.head)
            self.head = curr_head.next
            self.length -= 1
            return curr_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        self.length += 1
        new_node = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            curr_tail = self.tail
            self.tail = None
            self.head = None
            self.length = 0
            return curr_tail.value
        else:
            curr_tail = self.tail
            next_tail = self.tail.prev
            ListNode.delete(self.tail)
            self.tail = next_tail
            self.length -= 1
            return curr_tail.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if self.length == 0:
            return None
        elif self.length == 1:
            return None
        else: 
            curr_prev = node.prev
            curr_next = node.next
            curr_head = self.head
            ListNode.insert_before(curr_head, node)
            self.head = node
            node.next = curr_head
            node.prev = None
            if curr_prev:
                curr_prev.next = curr_next
            if curr_next:
                curr_next.prev = curr_prev


    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if self.length == 0:
            return None
        elif self.length == 1:
            return None

        else:
            curr_prev = node.prev
            curr_next = node.next
            curr_tail = self.tail

            if curr_prev:
                curr_prev.next = curr_next
            if curr_next:
                curr_next.prev = curr_prev
            if node == self.head:
                self.head = node.next

            ListNode.insert_after(curr_tail, node.value)
            self.tail = node
            node.prev = curr_tail
            node.next = None

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        delete_node = node
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        elif self.length == 2 and node == self.head:
            self.head = node.next
            self.length -= 1
        elif self.length == 2 and node == self.tail:
                self.tail = node.prev
                self.length -= 1

        else:
            if node.next is not None:
                node.next.prev = node.prev
            if node.prev is not None:
                node.prev.next = node.next
            if node == self.head:
                self.head = delete_node.next
            if self.tail == node:
                self.tail = node.prev
            self.length -= 1


    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head is None:
            return None

        curr_max = 0
        current_node = self.head
        while current_node:
            if current_node.value > curr_max:
                curr_max = current_node.value
            current_node = current_node.next
        return curr_max
