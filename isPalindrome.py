""" 234. Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """return True if the SLL is palindrome (same backward and forward)"""
        #first, if the sll empty or contain one elem, return True
        if not head or not head.next:
            return True
        
        #find midpoint using 2 pointers
        slow=fast=head
        while fast and fast.next: #once fast reaches the end, slow is at the midpoint
            slow = slow.next 
            fast = fast.next.next
        
        #reverse the second part of the sll from the midpoint(slow)
        prev = None #pointer prev set to none before starting to reverse

        while slow:
            next = slow.next #save the next node of slow before changing its reference
            slow.next = prev #change the direction to the curr node
            prev = slow #move prev to the curr node
            slow = next #move slow to the next node in the original ll

        #comapre the two halves
        p1 = head
        p2 = prev
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
