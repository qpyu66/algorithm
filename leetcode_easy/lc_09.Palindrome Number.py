"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
 

Constraints:

-2^31 <= x <= 2^31 - 1
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        lenx = len(strx)
        midlen = int(lenx/2)
        if x <0 : return False
    
        for i in range(0,midlen+1):
            ax = x // (10**i)
            bx = ax % 10
            print('ax, ',ax,'bx, ',bx,'x ',strx[i])
            if int(strx[i]) == bx:
                continue
            if int(strx[i]) != bx:
                return False
            
        return True     
      
            
s = Solution()
print(s.isPalindrome(1241))
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
