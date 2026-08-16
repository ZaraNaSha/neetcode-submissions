class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_con = 0
        num_set = set(nums)
        for n in nums:
            if n-1 not in num_set:
                tmp = 1
                while n+tmp in num_set:
                    #n += 1
                    tmp += 1
                if tmp > max_con:
                    max_con = tmp
        return max_con
        