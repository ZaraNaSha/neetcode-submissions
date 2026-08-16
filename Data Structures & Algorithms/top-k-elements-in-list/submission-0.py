class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k==0:
            return []
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1
        print(count)
        freq = [[] for i in range(len(nums)+1)]
        for n,cnt in count.items():
            freq[cnt].append(n)
        print(freq)
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res            
        return []


        