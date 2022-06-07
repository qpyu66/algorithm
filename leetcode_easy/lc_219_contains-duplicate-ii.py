"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

"""
#Time Limit Exceeded
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        print(nums,' k > ',k)
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] == nums[j]):
                    if(abs(i-j)<=k):
                        print('ok > ',abs(i-j))
                        return True
                    print('no > ',abs(i-j))
        return False

#code refactoring
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(list(set(nums))) == len(nums):
            return False
        
        for i in range(len(nums)):
            for j in range(1, k+1):
                if i+j > len(nums) -1:
                    continue
                if nums[i] == nums[i+j]:
                    return True
                
        return False
    
        
s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1],3)) #True
print(s.containsNearbyDuplicate([1,1,0,1],1)) #True
print(s.containsNearbyDuplicate([1,2,3,1,2,3],2)) #False


