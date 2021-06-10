"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1

"""

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nset = set(nums)
            
        for i in nset:
            n = nums.count(i)
            if n > len(nums)/2:
                print('n > ',n,i)
                return i
        

#code refactoring
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()    
        return nums[len(nums) >> 1]

#code refactoring
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]




s = Solution()
print(s.majorityElement([3,2,3]))    
print(s.majorityElement([2,2,1,1,1,2,2]))  