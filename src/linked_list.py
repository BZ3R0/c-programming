from node import Node


class LinkedList():
    def __init__(self):
        self.head = None
        self.len = 0

    def insert(self, key):
        node = Node(key, next=self.head)
        self.head = node
        self.len += 1

    def search(self, key):
        actual = self.head

        while actual is not None and actual.key != key:
            actual = actual.next

        return actual is not None

    def remove(self, key):
        actual = self.head

        if not actual:
            return False

        if actual.key == key:
            self.head = actual.next
        else:
            while actual is not None and actual.next is not None and actual.next.key != key:
                actual = actual.next

            if not actual.next:
                return
            else:
                actual.next = actual.next.next

        return actual is not None

    def __str__(self):
        if self.head is None:
            return 'List is empty'

        output = ''
        actual = self.head
        while actual is not None:
            output += 'key: ' + str(actual.key) + '\n' if actual.next != None else 'key: ' + str(actual.key)
            actual = actual.next

        return output