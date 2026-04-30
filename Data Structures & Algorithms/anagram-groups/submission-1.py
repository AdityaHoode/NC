# R1
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for i in range(len(strs)):
            if d["".join(sorted(strs[i]))] is None:
                d["".join(sorted(strs[i]))]=[]
            d["".join(sorted(strs[i]))].append(strs[i])
        op=[]
        for k,v in d.items():
            op.append(v)
        return op