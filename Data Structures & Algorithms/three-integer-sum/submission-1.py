class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n):
            left = i+1
            right = n-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return result    