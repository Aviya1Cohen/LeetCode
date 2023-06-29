""" 236. Lowest Common Ancestor of a Binary Tree
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1.  Output: 3
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4.  Output: 5
Input: root = [1,2], p = 1, q = 2.  Output: 1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #if no tree, return none
        if root is None:
            return  
        #if one of the nodes is the root, return root
        if root == p or root == q:
            return root
        
        #start recursion, check left and right
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        #if LCA is in one tree, return the other
        if not left:
            return right
        if not right:
            return left
            
        return root

    
        
