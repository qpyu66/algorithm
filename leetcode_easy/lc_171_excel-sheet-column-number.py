"""
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

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

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
Example 4:

Input: columnTitle = "FXSHRXW"
Output: 2147483647
 

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].

"""

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        lis = list(columnTitle) 
        ans=0    
        count = 0
        for i in lis[::-1]:
            ans += (ord(i)-64)*(26**count)
            count +=1
        return ans

s = Solution()
#print(s.titleToNumber("A")) #1  
#print(s.titleToNumber("AB"))  #28   
#print(s.titleToNumber("AZ")) #52
#print(s.titleToNumber("ZY"))  #701   
#print(s.titleToNumber("AAE")) #707   
#print(s.titleToNumber("FXSHRXW")) #2147483647