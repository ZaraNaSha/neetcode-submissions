class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        maxl = 0
        f = {}
        maxf = 0
        while r<len(s):
            f[s[r]] = f.get(s[r],0)+1
            maxf = max(maxf,f[s[r]])
            while r-l+1-maxf > k:
                f[s[l]] = f.get(s[l],0)-1
                l +=1
            maxl = max(maxl,r-l+1)
            r += 1
        return maxl
