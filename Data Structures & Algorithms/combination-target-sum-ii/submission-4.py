class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        subset = []
        candidates.sort()
        l = len(candidates)
        def dfs_func(i):
            tmp = sum(subset)
            if  tmp == target:
                res.add(tuple(subset))
                return
            elif i>=l or tmp > target:
                return
            subset.append(candidates[i])
            dfs_func(i+1)
            subset.pop()
            while i+1<l and candidates[i]==candidates[i+1]:
                i +=1
            dfs_func(i+1)
        dfs_func(0)
        return [list(r) for r in res]