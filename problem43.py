# This problem was asked by Amazon.

# Implement a stack that has the following methods:

# push(val), which pushes an element onto the stack
# pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
# max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
# Each method should run in constant time.

class Maxstack:
    def __init__(self):
        self.stack = []
        self.maxstack = []

    def push(val):
        self.stack.append(val)
        if self.maxstack:
            self.maxstack.append(max(val, self.maxstack[-1]))
        else:
            self.maxstack.append(val)

    def pop(self):
        if self.maxstack:
            self.maxstack.pop()
        return self.stack.pop()

    def max(self):
        return self.maxstack[-1]

    
        