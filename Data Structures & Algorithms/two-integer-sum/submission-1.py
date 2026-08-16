class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        # for i,n in enumerate(nums):
        #     a[n] = i
        # print(a)
        for i,n in enumerate(nums):
            tmp = target - n
            if tmp in a and a[tmp] != i:
                return [a[tmp],i]
            a[n] = i
        return []
        