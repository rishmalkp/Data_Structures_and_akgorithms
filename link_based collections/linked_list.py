"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element():
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList():
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_length(self):
        count=0
        itr = self.head

        while itr:
            count+=1
            itr=itr.next
        return count
        
        
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position<1 or position>self.get_length():
            return 'None'
        else:
            i=0
            itr=self.head
            while itr:
                if i==position-1:
                    return itr.value      
                itr = itr.next
                i+=1
        return None
            
        
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        newNode=new_element
        
        if position==1:
            newNode.next=self.head
            self.head=newNode
        else:
            itr = self.head
            for i in range(1, position-1):
                if(itr != None):
                    itr = itr.next   
            if(itr != None):
                newNode.next = itr.next
                itr.next = newNode 
    
    def delete(self, value):
        itr=self.head
        
        if itr is not None:
            if itr.value==value:
                self.head = itr.next
                itr=None
                return
        
        while itr is not None:
            if itr.data==value:
                break
            prev = itr
            itr=itr.next
        
        if itr==None:
            return
        
        prev.next = itr.next
        itr=None
        
        
#Set up some elements        
e1=Element(1)
e2=Element(2)
e3=Element(3)
e4=Element(4)

#Start setting up a LinkedList
ll=LinkedList(e1)
ll.append(e2)
ll.append(e3)

#should print1
print(ll.get_position(1))
#should print2
print(ll.get_position(2))

#Should print 3
print(ll.head.next.next.value)
#print Should also print 3
print(ll.get_position(3))


#test insert
ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(3))

#should print 3
print(ll.get_position(4))


#test delete
print(ll.delete(1))
print(ll.head.value)
#should print 2 now
print(ll.get_position(1))
print(ll.get_position(2))
print(ll.get_position(3))