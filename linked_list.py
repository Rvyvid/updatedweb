class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        new_node.prev = self.rear
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        return temp.data

    def __iter__(self):
        current = self.front
        while current:
            yield current.data
            current = current.next

class Deque:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def add_front(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def add_rear(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def remove_front(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        return temp.data

    def remove_rear(self):
        if self.is_empty():
            return None
        temp = self.rear
        self.rear = temp.prev
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None
        return temp.data

    def __iter__(self):
        current = self.front
        while current:
            yield current.data
            current = current.next
