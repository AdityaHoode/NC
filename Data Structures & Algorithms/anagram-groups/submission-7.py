# R1
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for word in strs:
            count=[0]*26
            for c in word:
                count[ord(c)-97]+=1
            key=tuple(count)
            d[key].append(word)
        return list(d.values())