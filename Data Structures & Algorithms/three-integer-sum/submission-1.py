class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,n in enumerate(nums):
            if n > 0:
                break
            if i>0 and nums[i-1]==n:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                tmp = n + nums[r] + nums[l]
                if tmp > 0:
                    r -= 1
                elif tmp <0:
                    l += 1
                else:
                    res.append([n,nums[r], nums[l]])
                    r -= 1
                    l += 1
                    while nums[l]==nums[l-1] and l<r:
                        l += 1
        return res
        