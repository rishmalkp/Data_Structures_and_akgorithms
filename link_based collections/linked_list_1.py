class Node():
    def __init__(self, a_number):
        self.data=a_number
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node=self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next=Node(value)

    def show_elements(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next
    
    def length(self):
        result=0
        current = self.head
        while current is not None:
            result+=1
            current=current.next
        return result
    
    def get_element(self, position):
        i=0
        current=self.head
        while current is not None:
            if i==position:
                return current.data
            current=current.next
            i+=1
        return None


list2=LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)
list2.append(9)
list2.show_elements()
list2.length()
list2.get_element(0)
#list2.head.data, list2.head.next.data, list2.head.next.next.data



#list1 = LinkedList()
#list1.head = Node(2)
#list1.head.next = Node(3)
#list1.head.next.next = Node(4)
#list1.head.data, list1.head.next.data, list1.head.next.next.data
#list1.head, list1.head.next, list1.head.next.next, list1.head.next.next.next



#Node()
#node1=Node()
#node1.data=2
#node2=Node()
#node2.data=3
#node3=Node()
#node3.data=5
#node4=Node()
#node4.data
#node4.data=10
#node1.data, node2.data, node3.data
