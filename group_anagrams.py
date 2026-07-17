from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            d[key].append(s)

        return list(d.values())