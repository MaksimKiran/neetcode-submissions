from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums)):
            target = -nums[i]
            seen = set()                      
            for j in range(i + 1, len(nums)):
                complement = target - nums[j]
                if complement in seen:
                    result.add(tuple(sorted((nums[i], complement, nums[j]))))
                seen.add(nums[j])
        return [list(t) for t in result]
