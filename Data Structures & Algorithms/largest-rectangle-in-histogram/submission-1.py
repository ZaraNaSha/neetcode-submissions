class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stacks = []
        maxs = 0
        heights.append(0)
        for i,h in enumerate(heights):
            w = 0
            while stacks and heights[stacks[-1]]>h:
                itmp = stacks.pop()
                w = i if not stacks else i-stacks[-1]-1
                maxs = max(maxs,heights[itmp]*w)
            
            stacks.append(i)
            
        return maxs
            

        