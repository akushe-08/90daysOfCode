from dsa.exceptions import EmptyStackException
from dsa.node_class import Node


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def is_empty(self):
        return not self.head

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def pop(self):
        if not self.head:
            raise EmptyStackException("Stack is Empty.")
        else:
            temp = self.head.value
            self.head = self.head.next
            self.length -= 1
            return temp

    def top(self):
        if self.head:
            return self.head.value
        return None

    def display(self):
        disp_string = ""
        if not self.head:
            print("Empty")
        else:
            temp = self.head
            while temp:
                disp_string += f"{temp.value}-->"
                temp = temp.next
            print(disp_string)

# stk = Stack()
# stk.push(23)
# stk.push(24)
# stk.push(25)
# stk.display()
# print(len(stk))
# stk.pop()
# stk.display()
# print(len(stk))
# print(stk.is_empty())
# stk.pop()
# stk.pop()
# print(stk.is_empty())
# stk.pop()
