"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = sorted(set(nums))
        nlen = len(n)
        if len(n) == 3:
            return (n[0])
        elif len(n) <3:
            return (n[-1])
        else:
            return (n[nlen-3])

#code refactoring1
class Solution1(object):
    def thirdMax(self, nums):
        nums = set(nums)
        nums = (sorted(nums))
        
        if (len(nums) >= 3):
            return nums[len(nums)-3]
        elif (len(nums) == 2):
            return nums[1]
        else:
            return nums[0]
        
        
#code refactoring2
class Solution2(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = sorted(set(nums))

        if len(arr) > 2:
            return arr[-3]
        else:
            return max(arr)


s = Solution()
print(s.thirdMax([3,2,1]))
print(s.thirdMax([2,3,2,1]))