class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0,len(heights)-1
        maxh = 0
        while l<r:
            tmp = min(heights[r],heights[l])*(r-l)
            maxh = max(maxh,tmp)
            if heights[l]<heights[r] :
                l += 1
            else:
                r -= 1
        return maxh


        