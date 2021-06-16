"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
Example 4:

Input: columnNumber = 2147483647
Output: "FXSHRXW"
 

Constraints:

1 <= columnNumber <= 231 - 1

"""


class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        n = columnNumber
        #나머지 0 아닐때
        if (n > 26 and n%26 != 0):
            ans = []
            s = ''
            while n>26:
                ans.insert(0,n%26)
                n = n//26
                if(n<27):
                    ans.insert(0,n)
            for i in ans:
                s += chr(i+64)          
            return s
        #나머지 0일때 z값
        elif(n/26 > 1 and n%26 == 0):
            s=''
            while (n/26>1):
                s+= 'Z'
                n -=1
                n = n//26
            s = chr(n+64)+s
            return s
        
        #26이하일때
        else:
            s = chr(n+64)
            return s




#code refactoring
class Solution:
    def convertToTitle(self, n: int) -> str:        
        res = ''
        num = n
        while num:
            res += chr((num-1)%26 + ord('A'))
            num = (num-1)//26
            
        return res[::-1]


s = Solution()
print(s.convertToTitle(1))   
print(s.convertToTitle(28))        
print(s.convertToTitle(701))     
print(s.convertToTitle(707))           

