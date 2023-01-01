from dsa.exceptions import EmptyQueueException, FullQueueException


class CircularQueue:
    def __init__(self, size):
        self.added_elements = 0
        self.rear = self.front = 0
        self.array = [None] * max(1, size)

    def _next(self, pos):
        pos += 1
        if pos == len(self.array):
            pos = 0
        return pos

    def is_empty(self):
        return self.added_elements == 0

    def is_full(self):
        return self.added_elements == len(self.array)

    def enqueue(self, value):
        if self.is_full():
            raise FullQueueException("Queue is full.")
        self.array[self.rear] = value
        self.rear = self._next(self.rear)
        self.added_elements += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueException("Queue is empty.")
        value = self.array[self.front]
        self.array[self.front] = None
        self.front = self._next(self.front)
        self.added_elements -= 1
        return value

    def display(self):
        print(self.array)


queue = CircularQueue(size=5)
queue.enqueue(12)
queue.enqueue(23)
queue.enqueue(56)
queue.enqueue(11)
queue.display()
queue.dequeue()
queue.display()
queue.enqueue(55)
queue.display()
queue.enqueue(66)
queue.display()
