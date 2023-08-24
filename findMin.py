"""
53. Find Minimum in Rotated Sorted Array
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        #initialize 2 pointers: start idx and end idx of the lst
        left, right = 0, len(nums)-1

        while left < right:
            #get middle idx
            mid = (left+right) // 2

            #if middle val greater than right val, minimum ele in the right side so search the right side
            if nums[mid] > nums[right]:
                left = mid + 1
            #otherwise, search the left side(include curr middle)
            else:
                right = mid

        return nums[left] #when loop is done, left will point the min elem so return that

