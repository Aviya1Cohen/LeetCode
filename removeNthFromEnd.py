"""
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use 2 pointers, set to head
        pointer1, pointer2 = head, head

        #places these pointers n nodes from each other (BY MOVING POINTER2)
        for i in range(n):            
            #loop until we reach the Nth node ( the end of the range n)
            pointer2 = pointer2.next  #move pointer2
        if not pointer2:
            return head.next

        #Then, inside while loop: while pointer.next 2 is not none:
        while pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next  
            
        pointer1.next = pointer1.next.next  # delete the nth elemen
        return head
