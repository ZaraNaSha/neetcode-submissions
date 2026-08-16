class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0,len(heights)-1
        maxh = 0
        while l<r:
            maxh = max(maxh,min(heights[r],heights[l])*(r-l))
            if heights[l]<heights[r] :
                l += 1
            else:
                r -= 1
        return maxh


        