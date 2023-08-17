"""
35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
"""

class Solution:
    def searchInsert(self, nums, target):
        #create pointers
        l, r = 0, len(nums)-1
        
        #while left less or equal to right
        while l <= r:
            #find middle point 
            mid = (l+r) // 2
            #if mid val less than target, move left to mid+1 
            if nums[mid] < target:
                l = mid + 1
            #elif mid greater than target, move right to mid-1
            elif nums[mid] > target:
                r = mid - 1
            else: #if mid==target
                return mid
            
        return l
