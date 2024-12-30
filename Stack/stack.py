class Stack:
    def __init__(self):
        self.s =[]

    def push(self,value):
        return self.s.append(value)

    def pop (self):
        if self.is_empty():
            print('stack is empty')
        else:
            return self.s.pop()
    
    def is_empty(self):
        if len(self.s) == 0:
            return True
        else:
            False

    def peak (self):
        if self.is_empty():
            print ("error")
            return None
        else :
            return self.s[-1]
        
    def size(self):
        return len(self.items)
        


stack= Stack()

stack.push(4)
stack.push(5)
stack.push('ahmed')
stack.pop()
stack.pop()
stack.pop()
print(stack.peak())
         