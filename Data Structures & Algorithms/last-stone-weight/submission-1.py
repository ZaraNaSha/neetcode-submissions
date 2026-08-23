class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) >= 2:
            tmp1 = heapq.heappop(stones)
            tmp2 = heapq.heappop(stones)
           # print(stones)
            if abs(tmp1)>abs(tmp2):
                heapq.heappush(stones,(abs(tmp1)-abs(tmp2))*-1)
            if len(stones) == 1:
                break
            if len(stones) == 0:
                return 0
        return stones[0]*-1

        