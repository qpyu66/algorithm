"""
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 104
"""

#0의개수구함 - 문제잘못이해
# class Solution:
#     def trailingZeroes(self, n: int) -> int:            
#         res=1
#         for i in range(1,n+1,1):
#             res *= i
#             #print('i > ',res)
#         print('res > ',res)
            
#         lis = list(str(res))
#         count=0
#         ans = lis.count('0')
#         print(ans)
            


#code refactoring
class Solution:
    def trailingZeroes(self, n: int) -> int:  
        ans = 0
        while n:
            n // 5
            ans += n
        return ans



    
s = Solution()
print(s.trailingZeroes(3))
print(s.trailingZeroes(5))
print(s.trailingZeroes(10))
print(s.trailingZeroes(7))


