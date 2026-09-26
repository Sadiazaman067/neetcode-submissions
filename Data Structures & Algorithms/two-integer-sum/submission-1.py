class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,nums in enumerate(nums):
            need = target-nums
            if need in seen:
                return [seen[need], i]
            seen[nums] = i
