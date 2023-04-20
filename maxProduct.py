"""
1464. Maximum Product of Two Elements in an Array

Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 
Example 1:
Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = 0 
    
        for i in range(len(nums)): #loop over the array
            for j in range(i+1, len(nums)): #loop over the array but start from the second element
                if (nums[i]-1)*(nums[j]-1) > res: #check if a pair is bigger than res
                    res = (nums[i]-1)*(nums[j]-1) #if so, update res

        return res
      
#print(maxProduct([3,4,5,2]))
