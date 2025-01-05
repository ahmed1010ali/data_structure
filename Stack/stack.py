class Stack:
    def __init__(self):
        self.s = []

    def push(self, value):
        self.s.append(value)

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
            return None
        else:
            return self.s.pop()

    def is_empty(self):
        return len(self.s) == 0

    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.s[-1]

    def size(self):
        return len(self.s)


# stack = Stack()

# stack.push(4)
# stack.push(5)
# stack.push('ahmed')
# stack.pop()
# stack.pop()
# print(stack.peak())  
# print(stack.is_empty())
