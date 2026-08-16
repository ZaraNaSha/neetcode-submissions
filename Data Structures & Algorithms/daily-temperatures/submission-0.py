class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tmp = []
        res = [0]*len(temperatures)
        for i,temp in enumerate(temperatures): 
            
            while tmp and temp > tmp[-1][1]:
                a = tmp.pop()
                #print(a[0])
                res[a[0]] = i-a[0]
            tmp.append((i,temp))
            #print(tmp)
        return res


        