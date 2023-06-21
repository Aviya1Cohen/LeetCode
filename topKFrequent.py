"""347. Top K Frequent Elements:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary to store element frequencies
        freq_dict = Counter(nums)
        
        # Create a heap to store the k most frequent elements
        heap = []
    
        # Iterate over unique elements in nums
        for num, frequency in freq_dict.items():
            # Insert element into the heap with frequency as key
            heapq.heappush(heap, (frequency, num)) #heapq.heappush -> like random.randint
            
            # If the heap size exceeds k, remove the smallest frequency element
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Extract the elements from the heap
        result = []
        for _, element in heap:
            result.append(element)
        
        return result
