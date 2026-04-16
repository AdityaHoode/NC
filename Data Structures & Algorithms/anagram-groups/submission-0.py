from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=dict()
        for i in range(len(strs)):
            d.setdefault(''.join(sorted(strs[i])),[]).append(strs[i])
        return list(d.values())