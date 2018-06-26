"""
Single linked list Double linked list Circular linked list
"""


class Node(object):
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class Sll(object):
    """ Singly Linked List """

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        """ Insert at head of list """

        new = Node(val)
        if self.head is None:
            self.head = new
        else:
            new.next = self.head.next
            self.head = new

    def pop(self):
        """ Delete from head of list """
        if self.head is None:
            return None

        val = self.head.data
        if self.head.next is None:
            # last node
            self.head = None

        return val

    def append(self, val):
        node = self.head
        while node.next is not None:
            node = node.next

        node.next = Node(val)

    def delete(self, val):
        if not self.head:
            return False

        prev = None
        curr = self.head
        while curr is not None:
            if curr.data == val:
                if curr == self.head:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                return True

            prev = curr
            curr = curr.next

        return False

class Dll(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        """
        Enqueue at end of the list
        :param val:
        :return:
        """
        new = Node(val)
        if self.head is None:
            self.tail = self.head = val
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = self.tail.next

    def dequeue(self, val):
        """
        Dequeue
        :param val:
        :return:
        """
        if self.head:
            node = self.head
            self.head = self.head.next
            return node

        return None

    def push(self, val):
        """

        :param val:
        :return:
        """
        pass
    def delete(self):
        pass

class Cll(object):
    def __init__(self):
        pass

