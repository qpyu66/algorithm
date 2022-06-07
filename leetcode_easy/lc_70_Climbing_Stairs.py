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
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        f1 = 1
        f2 = 2
        if n==1:
            return 1
        if n==2:
            return 2
        for i in range(2,n):
            fn = f1+f2
            f1=f2
            f2 = fn
        return fn


#code refactoring
class Solution1:
    def climbStairs(self, n: int) -> int:
        # strategy: implement recurrence
        # f(n) = f(n-1) + f(n-2)
        
        def clime(n):
            if n == 0:
                return 1
            if n == 1:
                return 1
            
            return clime(n - 1) + clime(n - 2)
        
        return clime(n)


       
    
s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(5))         

