class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs_func(i):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            elif i>=len(nums) or sum(subset) > target:
                return
            subset.append(nums[i])
            dfs_func(i)
            subset.pop()
            dfs_func(i+1)
        dfs_func(0)
        return res
            
            
        