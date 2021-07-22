"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
Example 4:

Input: n = 4
Output: true
Example 5:

Input: n = 5
Output: false
 

Constraints:

-231 <= n <= 231 - 1

"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        c =0
        while True:
            if 2 ** c == n:
                return True
            # 거듭제곱이 n 보다 크면 반복할 필요 없음
            if 2 ** c > n : 
                return False
            c +=1    
        return False   



#code refactoring
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if n == 
        if n <= 0:
            return False
        if n == 1:
            return True
        
        return n%2 == 0 and self.isPowerOfTwo(n/2)
                        
s = Solution()
print(s.isPowerOfTwo(1))   #True  
print(s.isPowerOfTwo(16))   #True  
print(s.isPowerOfTwo(3))    #False
print(s.isPowerOfTwo(8))    #True  