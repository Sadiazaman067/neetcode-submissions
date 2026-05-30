class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        max_left = [0] * n
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i-1])
        max_right = [0] * n
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])
            
            # step 3 - calculate water at each position
        total = 0
        for i in range(n):
            water = min(max_left[i], max_right[i]) - height[i]
            if water > 0:
                total += water
            
        return total