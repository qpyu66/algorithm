"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30

"""
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n=[]
        n.append([1])
        for i in range(1,numRows):
            n.append([1,1])
        
        for i in range(1,len(n)):
            for j in range(i+1):
                if(j == 0 or j == i):
                    n[i][j] = 1
                else:
                    n[i][j] = n[i-1][j-1] + n[i-1][j]
                    n[i].append(n[i][j])
        return n


#code refactoring
class Solution1:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        res = [[1]]
        
        for i in range(2, numRows+1):
            temp = [1]
            for j in range(1, i-1):
                temp.append(res[-1][j-1]+res[-1][j])
            
            temp += [1]
            res.append(temp)
        
        return res


        
s = Solution()
print(s.generate(5))