"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

"""

import time
from typing import List
start = time.time() 
#Error
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        dp = []
        for i in range(1, len(prices)):
            dp.append(prices[i]-prices[i-1])
        print(dp)

        maxp = 0
        minp = 0
        for j in range(len(dp)):
            minp = max(0, minp+dp[j])
            maxp = max(maxp, minp)
            print('>',minp,maxp)
        return maxp


#code refactoring
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        buy = sel = float("inf")
        for p in prices:
            if p < buy:
                buy = sel = p
            sel = max(sel, p)
            prof = max(prof, sel-buy)
        return prof
                

            
#code refactoring
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = 0
        current_min = prices[0]
        
        for price in prices:
            if price < current_min:
                current_min = price
            elif price - current_min > current_max: 
                current_max = price - current_min

        return current_max
        
#code refactoring
  """
7,1,5,3,6,0,4
4,2,5
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minima = 100_000
        max_profit = 0
        for price in prices:
            if price < minima:
                minima = price
            elif price-minima > max_profit:
                max_profit = price-minima
        return max_profit               
        



s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))   
#print("time :", time.time() - start) 
# print(s.maxProfit([7,6,4,3,1]))   
# print(s.maxProfit([1,2])) 
# print(s.maxProfit([1])) 
# print(s.maxProfit([1,2,4]))   












