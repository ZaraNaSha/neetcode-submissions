class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p,s = zip(*sorted(zip(position,speed),reverse=True))
        res = []
        for i in range(len(speed)):
            t = (target-p[i])/s[i]
            if not res:
                res.append(t)
            else:
                if res[-1] < t:
                    res.append(t)

        return len(res)
        