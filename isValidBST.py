"""98. Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
-The left subtree of a node contains only nodes with keys less than the node's key.
-The right subtree of a node contains only nodes with keys greater than the node's key.
-Both the left and right subtrees must also be binary search trees.

Input: root = [2,1,3], Output: true
Input: root = [5,1,4,null,null,3,6], Output: false
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """return True if it's a valid BST"""

        def valid(node, left, right):
            """Helper function to check BST validity within given boundaries"""
            if not node:  # If the tree is empty (base case), it is considered valid
                return True

            # Check if the current node value is within the specified boundaries
            if not(node.val < right and node.val > left):
                return False 

            # Recursively check the validity of the left and right subtrees
            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("inf"))
