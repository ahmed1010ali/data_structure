class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, value):
        self.q.append(value)

    def is_empty(self):
        return len(self.q)==0
    
    def dequeue (self):
        if self.is_empty():
            return None
        else :  
            return self.q.pop(0)

    def fort(self):
        if self.is_empty():
            return None
        else:
            return self.q[0]
    
    def size(self):
        return len(self.q)
    
    
# q = Queue()
# q.enqueue(2)
# q.enqueue(5)
# q.enqueue(3)
# q.dequeue()
# q.dequeue()
# q.dequeue()
# print(q.fort())