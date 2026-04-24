class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        result=1
        if nums==[]:
            return 0
        for n in nums:
            if n-1 not in s:
                length=1
                while n+1 in s:
                    length+=1
                    n+=1
                result=max(result, length)
        return result