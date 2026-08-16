class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl = 0
        tmp = []
        for c in s:
            if tmp and c in tmp:
                if maxl < len(tmp):
                    maxl = len(tmp)
                
                tmp = tmp[tmp.index(c)+1:]
            tmp.append(c)
        return max(maxl,len(tmp))

        