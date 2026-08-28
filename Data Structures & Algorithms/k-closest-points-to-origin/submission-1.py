class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        res1 = []
        for i in range(len(points)):
            tmp = points[i]
            d = -(tmp[0]**2+tmp[1]**2)
            heapq.heappush(res,[d,tmp[0],tmp[1]])
            if len(res)>k:
                heapq.heappop(res)
        while res:
            tmp = heapq.heappop(res)
            res1.append([tmp[1],tmp[2]])
        return res1
            


        