"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = []
        
        for i in nums:
            if i not in ans:
                ans.append(i)
            else:
                ans.remove(i)
        return ans[0]


#code refactoring
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        tracker = set()
        for num in nums:
            if num in tracker:
                tracker.remove(num)
            else:
                tracker.add(num)
        return tracker.pop()




#code refactoring
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans = nums[0]
        for i in range(1,len(nums)):
            ans ^=nums[i]
        return ans
        
        
s = Solution()
print(s.singleNumber([2,2,1]))    
print(s.singleNumber([4,1,2,1,2]))   