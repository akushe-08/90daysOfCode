class EmptyListException(Exception):
    pass


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_at_end(self, value):
        if not self.head:
            node = Node(value)
            self.head = node
        else:
            node = Node(value)
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    def insert_at_index(self, index, value):
        node = Node(value)
        if not self.head:
            self.head = node
        elif index == 0:
            self.insert_at_beginning(value)
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            node.next = temp.next
            temp.next = node

    def delete(self, index=None):
        if not self.head:
            raise EmptyListException("No elements to delete.")
        elif not index or index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next

    def display(self):
        disp_string = ""
        temp = self.head
        while temp:
            disp_string += f"{temp.value}-->"
            temp = temp.next
        print("Empty") if not disp_string else print(disp_string)
        print("\n")


ll = LinkedList()
ll.insert_at_end(12)
ll.insert_at_end(13)
ll.insert_at_beginning(11)
ll.insert_at_end(14)
ll.insert_at_end(15)
ll.insert_at_end(16)
ll.display()
ll.insert_at_index(2, 22)
ll.display()
ll.insert_at_index(0, 55)
ll.display()
ll.delete(2)
ll.display()
ll.delete()
ll.display()
ll.delete(3)
ll.display()
ll.delete()
ll.display()
ll.delete()
ll.display()
ll.delete()
ll.display()
ll.delete()
ll.display()
ll.delete()
ll.display()
ll.delete()
