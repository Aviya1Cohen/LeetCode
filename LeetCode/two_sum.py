"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
-You may assume that each input would have exactly one solution, and you may not use the same element twice.
-You can return the answer in any order.

Example 1: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2: nums = [3,2,4], target = 6
Output: [1,2]
"""

def two_sum(nums, target):
    seen = {}   #{num: idx}

    for i, num in enumerate(nums):
        answer = target - num
        if not answer in seen:
            seen[num] = i   #add the num and its idx to the dict
        else:
            return(i, seen.get(answer))