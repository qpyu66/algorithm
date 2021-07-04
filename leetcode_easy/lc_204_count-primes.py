"""
Count the number of prime numbers less than a non-negative number, n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106

"""

#Time Limit Exceeded
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         count = 0
#         for i in range(2,n):
#             for j in range(2,i):
#                 if i%j == 0:
#                     break
#             else:
#                 count += 1
#         return count

#Sieve of Eratosthenes 에라토스테네스의 체
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         ans = [True] * n
#         m = int(n ** 0.5) #루트
#         for i in range(2,m+1):
#             if ans[i] == True: #i가 소수일 때
#                 for j in range(i+i,n,i): #i 이후의 배수 false
#                     ans[j] = False
#         res = []
#         for i in range(2,n):
#             if ans[i] == True:
#                 print(i)
#                 res.append(i)
#         return len(res)


s = Solution()
print(s.countPrimes(10))
print(s.countPrimes(4))