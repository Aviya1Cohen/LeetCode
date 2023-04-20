"""
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        if len(unique) == len(nums):
            return False
        return True
