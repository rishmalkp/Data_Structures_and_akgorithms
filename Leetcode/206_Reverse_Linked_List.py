'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

#Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if head is None:
            return head
        prev_node = head
        node = prev_node.next
        prev_node.next = None
        while node is not None:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
        return prev_node