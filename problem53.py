class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def push(self, val):
        n = Node(val)
        if self.count == 0:
            self.head = n
            self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
        self.count +=1

    def pop(self):
        if self.count == 0:
            return None
        
        item = self.tail
        self.tail = self.tail.prev
        self.count -=1
        return item.value

class queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, val):
        self.stack1.push(val)

    def dequeue(self):
        if self.stack2.count == 0:
            while self.stack1.count > 0:
                self.stack2.push(self.stack1.pop())
        
        return self.stack2.pop()

q = queue()
q.enqueue(10)
q.enqueue(6)
q.enqueue(7)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())