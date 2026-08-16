class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)
        
        for c in s1:
            cnt1[c] += 1
        
        r,l = 0,0
        f = {}
        while r < len(s2):
            if s2[r] in s1:
                c = s2[r]
                cnt2[c] += 1
                #print(cnt2)
                if r-l+1 == len(s1):
                    if cnt1==cnt2:
                        return True
                    cnt2[s2[l]] -= 1
                    l += 1
            else:
                l = r+1
                cnt2 = defaultdict(int)
            r +=1
            #print(l,r)
                
        return False

            

        