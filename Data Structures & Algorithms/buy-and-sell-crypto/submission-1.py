class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minb = prices[0]
        for p in prices:
            maxp = max(maxp, p-minb)
            minb = min(p,minb)
        return maxp
        