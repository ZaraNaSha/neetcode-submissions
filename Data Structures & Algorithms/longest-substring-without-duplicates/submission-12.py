class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp = {}
        l,r=0,0
        maxl = 0
        while r < len(s):
            if s[r] in tmp:
                l = max(tmp[s[r]]+1,l)
            tmp[s[r]] = r
            maxl = max(maxl, r-l+1)
            r += 1
        return maxl
        
        