"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nlen = len(nums)
        p = 0
       
        for i in range(len(nums)):
            nnums = nums[i]
            if nnums != 0:
                temp = nums[i]
                nums[i] = nums[p]
                nums[p] = temp
                p += 1

        return nums
                
        
        
#code refactoring
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        num_len = len(nums)
        nums[:] = [x for x in nums if  x != 0]
        nums += [0] * (num_len - len(nums))
        
        
        
#code refactoring       
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=0
        r=0
        for i in range(len(nums)):
            if(nums[r]==0):
                r+=1
            else:
                nums[r],nums[l]=nums[l],nums[r]
                l+=1
                r+=1
        return nums        
        
        
s = Solution()
print(s.moveZeroes([0,1,0,3,12]))
# print(s.moveZeroes([0]))        
