""" 198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it 
will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob
tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        tempDict = {} # create a dictionary for memoization
        return self.robHelper(nums, 0, tempDict)
    
    def robHelper(self, nums: List[int], currIndex: int, tempDict: dict) -> int:
        # base case - if the len of houses is the same as idx or less, return 0 (no houses)
        if currIndex >= len(nums):
            return 0
        # if the result is already calculated, return it from the tempDict
        if currIndex in tempDict:
            return tempDict[currIndex]
        
        # recursive call, check 2 options
        stealFirstHouse = nums[currIndex] + self.robHelper(nums, currIndex + 2, tempDict)
        skipFirstHouse = self.robHelper(nums, currIndex + 1, tempDict)
        
        # store the max in tempDict
        tempDict[currIndex] = max(stealFirstHouse, skipFirstHouse)
        
        return tempDict[currIndex]
