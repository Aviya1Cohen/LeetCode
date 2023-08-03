""" 206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = None #assign dummy to none to use as the new head 
        curr = head #assign curr to head

        while curr:
            nextNode = curr.next #store the next node
            curr.next = dummyHead #the next node becomes the head (start traversal)
            dummyHead = curr #assign dummy to curr since it'll be the prev node 
            curr = nextNode #move tto he next node in the original ll
        return dummyHead
