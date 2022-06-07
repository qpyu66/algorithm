"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.


"""

#이진수->십진수
#십진수 더하기
#십진수->이진수
#28ms
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        inta = int(a,2)
        intb = int(b,2)
        sumab = inta+intb
        formab = format(sumab,'b')
        #print(inta,intb,sumab,formab)
        return formab
        
        
#code refactoring // 24ms
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         num_a = int(a, 2)
#         num_b = int(b, 2)
#         return str(bin(num_a + num_b))[2:]


#code refactoring // 20 ms
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         result, carry = "", "0"
#         i, j = len(a)-1, len(b)-1
#         while i >= 0 and j >= 0:
#             if a[i] == b[j] == "1":
#                 result = carry + result
#                 carry = "1"
#             elif a[i] == b[j] == "0":
#                 result = carry + result
#                 carry = "0"
#             elif carry == "0":
#                 result = "1" + result
#             else:
#                 result = "0" + result
#             i -= 1
#             j -= 1
                
#         while i >= 0:
#             if a[i] == carry =="1":
#                 result = "0" + result
#                 carry = "1"
#             elif a[i] == carry =="0":
#                 result = "0" + result
#             else:
#                 result = "1" + result
#                 carry = "0"
#             i -= 1
                
#         while j >= 0:
#             if b[j] == carry =="1":
#                 result = "0" + result
#                 carry = "1"
#             elif b[j] == carry =="0":
#                 result = "0" + result
#             else:
#                 result = "1" + result
#                 carry = "0"
#             j -= 1
                
#         if carry == "1":
#             result = "1" + result
        
#         return result






s = Solution()
print(s.addBinary("11","1"))
print(s.addBinary("1010","1011"))
