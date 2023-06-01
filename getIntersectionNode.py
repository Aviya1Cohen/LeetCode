"""160. Intersection of Two Linked Lists
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

example: Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
         Output: Intersected at '8'
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
pseudocode:
1. Get the length of each list: traverse the list and count the number of nodes.
2. Take the longer list and subtract the shorter list's length to get the difference.
3. Move the pointer of the longer list forward by the difference in lengths.
4. Traverse both lists together until the pointers meet, indicating the intersection point.
5. Return the common first node where the pointers meet.
#if the two linked lists have no intersection at all, return None
"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """return the node at which the two lists intersect(the first common node)"""
        #get the length of listA
        currA = headA 
        lenA = 0 
        while currA: 
            lenA += 1 
            currA = currA.next 
        #get the length of listB
        currB = headB
        lenB = 0
        while currB:
            lenB += 1
            currB = currB.next

        #find longer list
        longer = headA if lenA > lenB else headB
        #find shorter
        shorter = headB if lenB < lenA else headA
        
        #clculate the difference in lengths
        diff = abs(lenA - lenB)

        # Move the longer list pointer 'diff' steps ahead
        for _ in range(diff):
            longer = longer.next

        # Traverse both lists until they meet at the intersection point
        while shorter != longer:
            shorter = shorter.next
            longer = longer.next

        # Return the intersection node
        return longer

      
#another solution      
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #initializing pointers
        currA = headA
        currB = headB

        #traverse the lists until lists intersect or ends
        while currA != currB: 
            #move to next, else if currA reach the end of listA, switch to listB
            currA = currA.next if currA else headB 
            #move to next, else if currB reach the end of listB, switch to listA
            currB = currB.next if currB else headA
            
        #return the intersection node, or None if there's no intersection
        return currA
