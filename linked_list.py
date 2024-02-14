class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def append_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove_first(self):
        if not self.head:
            raise ValueError('Linked list is empty')
        self.head = self.head.next

    def remove_last(self):
        if not self.head:
            raise ValueError('Linked list is empty')
        if not self.head.next:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def remove_at(self, index):
        if index < 0 or not self.head:
            raise ValueError('Invalid index or linked list is empty')
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if not current.next:
                raise ValueError('Index out of range')
            current = current.next
        if not current.next:
            raise ValueError('Index out of range')
        current.next = current.next.next

    def remove_first_value(self, value):
        if not self.head:
            raise ValueError('Linked list is empty')
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
        raise ValueError('Value not found')

    def remove_last_value(self, value):
        if not self.head:
            raise ValueError('Linked list is empty')
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == value and not current.next.next:
                current.next = None
                return
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
        raise ValueError('Value not found')


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
