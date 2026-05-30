class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        seen = set()
        left = 0
        right = 0
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                max_length = max(max_length, right - left + 1)
                right+=1
            elif s[right] in seen:
                 seen.remove(s[left])
                 left+=1           
            
        return max_length