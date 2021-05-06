"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1

"""


#36ms
class Solution:
    def reverse(self, x: int) -> int:
       
        a = list(str(x))
        if x <0:
            b = a[1:]
            c = b[::-1]
            r = ''.join(c)
            ans = int(r)*-1
            if ans <  2**31*-1:
                return 0
            else:
                return ans
        else:
            b = a[::-1]
            ans = int(''.join(b))
            if ans > 2**31:
                return 0
            else:
                return ans


#code refactoring 24ms
# class Solution:
#     def reverse(self, x: int) -> int:
#         # print(2**31-1)
       
        
#         if x>0:
#             x=int(str(x)[::-1])
#         if x<0:
#             x=-1*int(str(-x)[::-1])
            
#         if x < -2**31:
#             return 0
#         if x > 2**31-1:
#             return 0
#         return x
                



s = Solution()
#print(s.reverse(123))
print(s.reverse(-123))        
print(s.reverse(120))