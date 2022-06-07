"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
"""
#32ms
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n=[]
        n.append([1])
        for i in range(1,rowIndex+1):
            n.append([1,1])
        
        for i in range(1,len(n)):
            for j in range(i+1):
                if(j == 0 or j == i):
                    n[i][j] = 1
                else:
                    n[i][j] = n[i-1][j-1] + n[i-1][j]
                    n[i].append(n[i][j])
            
        return n[-1]



#code refactoring 24ms
class Solution1:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [1]*(rowIndex + 1)
        for i in range(2,rowIndex+1):
            for j in range(i-1,0,-1):
                pascal[j] += pascal[j-1]
        return pascal



#code refactoring 16ms       
class Solution2:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        res = [1]*(rowIndex+1)
        for i in range(1,rowIndex):
            for j in range(i,0,-1):
                res[j]+=res[j-1]
                
        return res



s = Solution()
print(s.getRow(3))