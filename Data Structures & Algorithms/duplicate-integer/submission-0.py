class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newSet = []
        for num in nums:
            if num not in newSet:
                newSet.append(num)
            else:
                return True
        return False