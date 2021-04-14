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
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        inta = int(a,2)
        intb = int(b,2)
        sumab = inta+intb
        formab = format(sumab,'b')
        #print(inta,intb,sumab,formab)
        return formab
        
        
s = Solution()
print(s.addBinary("11","1"))
print(s.addBinary("1010","1011"))
