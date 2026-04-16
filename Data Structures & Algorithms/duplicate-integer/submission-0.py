class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sn = sorted(nums)
        for i in range(len(sn)-1):
            if sn[i] == sn[i+1]:
                return True
        return False