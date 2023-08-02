""" 21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1) #init a dummy head to start the merge list
        curr = dummy_head #assign curr to dummy to traverse 

        while list1 and list2: #loop until one of the two is empty
            if list1.val <= list2.val: #if the node is l2 is less or equal
                curr.next = list1 # add to merge lst
                list1 = list1.next # move list 1 to its next node
            else: #same for list 2
                curr.next = list2
                list2 = list2.next
            curr = curr.next 
            
        #continue until one of the lsts is empty
        #then add the remaining nodes from the other lst to the merge lst
        curr.next = list1 if list1 else list2

        #return next as the head of the merge lst
        return dummy_head.next
