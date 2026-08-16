class Solution:
    def isValid(self, s: str) -> bool:
        char_v = {')':'(','}':'{',']':'['}
        tmp = []
        for c in s:
            if c in char_v.values():
                tmp.append(c)
            else:
                #print(tmp)
                if len(tmp)==0:
                    return False
                if tmp.pop() != char_v[c]:
                    return False

        return len(tmp)==0

        