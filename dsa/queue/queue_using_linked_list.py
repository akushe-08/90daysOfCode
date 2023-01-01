from dsa.linked_list.main import LinkedList
from dsa.exceptions import EmptyListException


class Queue:
    def __init__(self):
        self.list = LinkedList()

    def __len__(self):
        return self.list.__len__()

    def enqueue(self, value):
        self.list.insert_at_end(value)

    def dequeue(self):
        if self.list.length == 0:
            raise EmptyListException("Queue is empty.")
        return self.list.delete()

    def is_empty(self):
        return self.list.length == 0

    def display(self):
        self.list.display()


queue = Queue()
queue.enqueue(12)
queue.display()
queue.enqueue(23)
queue.display()
print(len(queue))
queue.dequeue()
queue.display()
print(len(queue))
