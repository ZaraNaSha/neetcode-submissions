class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minb = prices[0]
        for p in prices:
            if maxp < p-minb :
                maxp = p-minb
            if p < minb: 
                minb = p
        return maxp
        