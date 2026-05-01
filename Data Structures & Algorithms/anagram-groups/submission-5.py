# R1
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for i in range(len(strs)):
            count=[0]*26
            for j in strs[i]:
                count[ord(j)-97]+=1
            t=tuple(count)
            d[t].append(strs[i])
        return list(d.values())