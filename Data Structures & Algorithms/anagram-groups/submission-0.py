from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_list = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            new_list[key].append(s)

        return list(new_list.values())