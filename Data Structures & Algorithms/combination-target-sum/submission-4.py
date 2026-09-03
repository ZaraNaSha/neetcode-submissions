class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        l = len(nums)
        def dfs_func(i):
            tmp = sum(subset)
            if  tmp == target:
                res.append(subset.copy())
                return
            elif i>=l or tmp > target:
                return
            subset.append(nums[i])
            dfs_func(i)
            subset.pop()
            dfs_func(i+1)
        dfs_func(0)
        return res
            
            
        