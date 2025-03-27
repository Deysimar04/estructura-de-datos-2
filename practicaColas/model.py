class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node

    def dequeue(self):
        if not self.head:
            return None
        item = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return item

    def is_empty(self):
        return self.head is None

from model import Queue

class TicketController:
    def __init__(self):
        self.queue = Queue()

    def add_ticket(self, ticket):
        self.queue.enqueue(ticket)

    def get_next_ticket(self):
        # Prioritize tickets with priority_attention = True
        current = self.queue.head
        previous = None
        while current:
            if current.data.priority_attention:
                if previous:
                    previous.next = current.next
                else:
                    self.queue.head = current.next
                if current == self.queue.tail:
                    self.queue.tail = previous
                return current.data
            previous = current
            current = current.next
        # If no priority tickets, return the first ticket in the queue
        return self.queue.dequeue()