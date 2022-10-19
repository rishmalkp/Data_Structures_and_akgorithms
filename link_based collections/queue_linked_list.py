class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
        
class Queue:
    def __init__(self):
        self.top=None
        self.last=None
        
    def enqueue(self, value):
        if self.last is None:
            self.top=Node(value)
            self.last=self.top
        else:
            self.last.next = Node(value)
            self.last=self.last.next
            
    def dequeue(self):
        if self.top is None:
            return None
        else:
            to_return=self.top.value
            self.top=self.top.next
            return to_return

a_queue=Queue()
a_queue.enqueue(1)
a_queue.enqueue(2)
a_queue.enqueue(3)
a_queue.enqueue(4)
a_queue.enqueue(5)
#should be 1
print(a_queue.top.value)
a_queue.dequeue()
#should be 2
print(a_queue.top.value)