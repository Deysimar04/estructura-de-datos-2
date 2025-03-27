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