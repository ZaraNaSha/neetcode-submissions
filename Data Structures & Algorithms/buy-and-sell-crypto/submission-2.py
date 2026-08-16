class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mmax = 0
        for i in range(len(prices)):
            l = i + 1
            while l < len(prices):
                tmp = prices[l]-prices[i]
                if mmax < tmp:
                    mmax = tmp
                l += 1
        return mmax



        