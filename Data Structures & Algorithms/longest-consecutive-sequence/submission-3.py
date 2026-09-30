class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxl = 0
        nums = set(nums)
        for num in nums:
            if (num - 1) not in nums:
                l = 1
                cnd = num + 1
                while (cnd) in nums:
                    cnd = cnd + 1
                    l = l + 1
                maxl = max(maxl, l)
        return maxl
