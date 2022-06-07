"""
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.

"""
from typing import List


# Time Limit Exceeded
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#          for i in range(len(numbers)-1):
#             for j in range(i+1,len(numbers)):
#                 if(numbers[i] + numbers[j] == target):
#                     return i+1,j+1



#code refactoring
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i=0
        j=n-1
        while i<j:
            s = numbers[i] + numbers[j]
            if s == target:
                return i+1,j+1
            elif s<target:
                i += 1
            else:
                j -=1
        return -1, -1



#code refactoring
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        
        while i != j:
            if numbers[i] + numbers[j] == target:
                return([i+1, j+1])
            elif numbers[i] + numbers[j] > target:
                j = j - 1
            else:
                i = i + 1


        
s = Solution()
#print(s.twoSum([2,7,11,15],9))
#print(s.twoSum([2,3,4],6))
print(s.twoSum([-1,0],-1))
