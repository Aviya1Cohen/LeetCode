"""
83. Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
Input: head = [1,1,2]
Output: [1,2]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #first, check the list is not empty
        if not head:
            return
        else: 
            curr = head #start from the head
            while curr.next: #while curr next is not None
                if curr.val == curr.next.val: #if we have a duplicate, delete its next
                     curr.next = curr.next.next 
                else: #else, continue to the next node
                    curr = curr.next
            return head
