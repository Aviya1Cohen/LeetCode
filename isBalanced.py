""" 110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

Input: root = [3,9,20,null,null,15,7], Output: true
Input: root = [1,2,2,3,3,null,null,4,4], Output: false
Input: root = [], Output: true
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """return true if left and right subtrees differ by at most one"""
        if not root: #if root is none, it's valid
            return True
        #calc height of left and right subtrees
        leftHeight = self.helper(root.left)
        rightHeight = self.helper(root.right)
        #if the absolute diff between the heights is more than 1, its not balances
        if abs(leftHeight - rightHeight) > 1:
            return False
        #recursively check if the subtrees are balanced 
        return self.isBalanced(root.left) and self.isBalanced(root.right)


    def helper(self, node):
        """helper function to get the height"""
        if not node:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        return max(left, right) + 1 #return max height plus 1 for curr node
