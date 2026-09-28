class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # buckets[f] = list of numbers that appear exactly f times
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, freq in count.items():
            buckets[freq].append(n)

        # walk from highest frequency down, grab until we have k
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for n in buckets[freq]:
                result.append(n)
                if len(result) == k:
                    return result