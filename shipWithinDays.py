""" 1011. Capacity To Ship Packages Within D Days
A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt 
(in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
"""

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """return the minimum ship capacity to ship all packages within 'days'"""
        #initialize search range:
        #l - weight of the heaviest package, r - the sum of all package weights
        l, r = max(weights), sum(weights)
        #initialize res to r (sum of all packages)
        res = r

        def canShip(cap):
            """helper - check if it's possible to ship all packages within a given capacity"""
            #initialize ships count and current capacity
            ships, currcap = 1, cap
            for w in weights:
                #if curr pack can't fit in curr capacity, increase ship counts
                if currcap - w < 0:
                    ships += 1
                    currcap = cap #reset curr capacity to the max allowed             
                currcap -= w #subtract package weight from the curr capacity
            #return true if it's possible to ship within 'days' days.
            return ships <= days

        #binary search to find min capacity
        while l <= r:
            cap = (l+r)//2 #calc middle
            #if it's possible to ship with curr capacity, update res to min capacity found so far
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1 #update right
            else:
                l = cap + 1 #update left

        return res 
                
