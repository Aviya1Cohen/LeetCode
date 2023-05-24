# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]: 
        if not head: #check SLL not empty
            return 
        
        # Create two dummy nodes to hold the smaller and greater nodes
        smaller_head = ListNode(0)
        greater_head = ListNode(0)
        smaller_tail = smaller_head
        greater_tail = greater_head

        curr = head #traverse the original LL

        while curr:
            if curr.val < x:
                smaller_tail.next = curr #append the curr node to the smaller values list
                smaller_tail = smaller_tail.next #move the tail pointer       
            else:
                greater_tail.next = curr #append the curr node to the greater/equal values list
                greater_tail = greater_tail.next #move the tail pointer   

            curr = curr.next # move to the next node in the original LL

        #connect the greater list to the end of the smaller list
        smaller_tail.next = greater_head.next

        #set the tail of the greaters to None to indicate to end of the list
        greater_tail.next = None

        #return the head of the smaller values list as the partitioned LL
        return smaller_head.next
