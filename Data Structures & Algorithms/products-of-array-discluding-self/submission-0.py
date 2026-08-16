class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        s = 0
        for n in nums:
            if n==0:
                s +=1
            else:
                p = p*n
        if s>1:
            return [0]*len(nums)
        res = [0] * len(nums)
        for i,c in enumerate(nums):
            if s: 
                res[i]=0 if c else p
            else:
                res[i] = p//c
        return res

        