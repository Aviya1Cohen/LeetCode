"""
257. Binary Tree Paths
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
            
        def helper(root, path):
            if not root: #if not root return none
                return 
                
            path += str(root.val) # append the curr node's val to the path
            
            #if curr node is a leaf, append the path to res
            if not root.left and not root.right:
                res.append(path)
                return

            # if not a leaf node, continue with left and right children
            if root.left:
                helper(root.left, path + "->")
            if root.right:
                helper(root.right, path + "->")

        
        if root: #check bst is not empty
            helper(root, "")
        
        return res
