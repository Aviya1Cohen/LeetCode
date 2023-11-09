"""1022. Sum of Root To Leaf Binary Numbers
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.
The test cases are generated so that the answer fits in a 32-bits integer.

Example 1:
Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, binaryStr):
            #if node is none return 0
            if not node:
                return 0
            #update binary str
            binaryStr = binaryStr + str(node.val) #add to the binary number

            #if its leaf, return the decimal val oof the binary str
            if not node.left and not node.right:
                return int(binaryStr, 2)
            
            #recursion
            left_sum = dfs(node.left, binaryStr)
            right_sum = dfs(node.right, binaryStr)
            return left_sum+right_sum
        
        return dfs(root, "")

