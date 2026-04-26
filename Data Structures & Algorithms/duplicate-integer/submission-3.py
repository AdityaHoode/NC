# R1

from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        if c == {}:
            return False
        elif c.most_common(1)[0][1] > 1:
            return True
        return False