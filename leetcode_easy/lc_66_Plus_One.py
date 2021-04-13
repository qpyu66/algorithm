"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
"""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        si = [str(int) for int in digits]
        djoin = ''.join(si)
        #print(djoin)
        #print(type(djoin))
        dint = int(djoin)
        print(dint, type(dint))
        a = dint + 1
        print(a,type(a))
        return list(str(a))
       
        
        
s = Solution()
print(s.plusOne([1,2,3]))
print(s.plusOne([4,3,2,1]))
print(s.plusOne([0]))
print(s.plusOne([9]))
print(s.plusOne([1,9]))
print(s.plusOne([9,9])) #[1,0,0]
