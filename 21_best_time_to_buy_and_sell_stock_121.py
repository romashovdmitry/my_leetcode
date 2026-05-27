from typing import List
from print_and_sleep import print_and_sleep

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = prices[0]
        max_dif = 0

        for price in prices:

            min_value = min(price, min_value)
            max_dif = max(max_dif, price-min_value)

        return max_dif


prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))

prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))

prices = [1,3,2,10]
print(Solution().maxProfit(prices))

