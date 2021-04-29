class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j]) == target:
                    #print('1 i,j > ',i,j,nums[i] + nums[j])
                    return(i,j)




s = Solution()
#print(s.twoSum([2,7,11,15],9))
print(s.twoSum([3,2,4],6))
