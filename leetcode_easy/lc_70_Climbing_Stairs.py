"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

"""
#Time Limit Exceeded
#Recursion with memoization
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def clim(n):
            if (n < 3):
                return n
            
            else:
                return clim(n-1)+clim(n-2)
        
        return clim(n)


#Time Limit Exceeded
#fibonacci
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = {1:1,2:2}
        if n in ans:
            return ans[n]
        else:
            res = self.climbStairs(n-1)+self.climbStairs(n-2)
            ans[n] = res
            return res
       
    
s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(5))         

