""" 33. Search in Rotated Sorted Array
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """return idx od target if in nums else -1"""
        #assign left and right pointers to the start and end 
        left, right = 0, len(nums) - 1

        #binary search
        while left <= right:
            #calc middle
            middle = (left+right) // 2
            #check if middle is target
            if nums[middle] == target:
                return middle 
            #check if left is sorted 
            if nums[left] <= nums[middle]:
                #check if target in between the range of sorted left
                if nums[left] <= target < nums[middle]:
                    #update right to search in left
                    right = middle - 1
                else: #update left to search in right
                    left = middle + 1
            #if the left unsorted, the right sorted
            else:
                #check if target between the range of sorted right
                if nums[middle] < target <=nums[right]:
                    #update left to search in right
                    left = middle + 1
                else: #update right to search in left
                    right = middle -1

        #if not found, return -1
        return -1
        
nums = [4,5,6,7,0,1,2]
target = 0 #4
solution = Solution()
result = solution.search(nums, target)
print(result)
