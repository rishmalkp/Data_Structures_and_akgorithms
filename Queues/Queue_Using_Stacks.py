'''
Implementation of a queue using stack is very important.
we have access to stacks push and pop operations. Using those we need to execute queue's and
dequeue operation. it can be done in two ways, by either making the enqueue operation costly
()(n)) or the dequeue operation costly(O(n)). In the first method, we need two stacks s1 and
s2 and we have maintain them such that the element entered first is always at the top iof the
stack s1. This way, for dequeue, we just need to pop from s1.
But for enqueueing , we have to make the enqueued item reach the bottom of the stack.
For that, we will have to pop the elements of s1 one by one and push them onto stack 2, then
add the new item to stack 1, And then again pop everything from stack2 and push it back to s1.
So the new item at the last.
'''


class Queue():
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []

    def peek(self):
        if len(self.s1) == 0:
            print("Queue empty")
        else:
            return self.s1[len(self.s1)-1]#display top object from the stack
        
    def enqueue(self, data):
        for i in range(len(self.s1)):#move all elements from stack 1 to stack 2
            item = self.s1.pop()
            self.s2.append(item)#it will be reversed order in stack 2
        self.s1.append(data)#add new element to stack 1 fyi:empty list
        for i in range(len(self.s2)):#move back all elements to stack 1
            item = self.s2.pop()
            self.s1.append(item)
        return

    def dequeue(self):
        if len(self.s1) == 0:
            print("Queue is empty")
        else:
            return self.s1.pop()#will return first element enter into this queue

    def print_queue(self):
        if len(self.s1) == 0:
            print("Queue is empty")
            return
        for i in range(len(self.s1) - 1, 0, -1):
            print(f'{self.s1[i]} <<-- ', end='')
        print(self.s1[0])#to print first value in the list, aka last in queue
        return


my_queue = Queue()
my_queue.enqueue(2)
my_queue.enqueue(4)
my_queue.enqueue(0)
my_queue.print_queue()

my_queue.dequeue()
my_queue.print_queue()

print(my_queue.peek())

my_queue.enqueue(9)
my_queue.print_queue()

my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()

'''
For the second method, we can make the dequeue operation costly just like we did with enqueue
operation above.
For enqueueing, we will simply push in s1
For dequeueing, we will pop all but last element of s1 and push into s2. Then we will pop the 
last element of s1, Which is the element we want dequeue. After that we pop all items of s2
and push it back into s1.
This makes dequeue operation O(n) while enqueue and peek remain O(1).
'''