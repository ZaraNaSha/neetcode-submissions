class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        leni = 0
        for i in nums:
            a.add(i)
            leni += 1
            if leni != len(a):
                return True
        return False
        