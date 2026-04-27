# R1

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sc = Counter(s)
        for ch in t:
            if sc[ch]-1<0:
                return False
            sc[ch]-=1
        return True