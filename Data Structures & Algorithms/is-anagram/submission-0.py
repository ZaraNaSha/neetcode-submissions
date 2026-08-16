class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        cnts , cntt = {},{}
        for i in range(len(s)):
            cnts[s[i]] = cnts.get(s[i],0)+1
            cntt[t[i]] = cntt.get(t[i],0)+1
        return cnts==cntt
        