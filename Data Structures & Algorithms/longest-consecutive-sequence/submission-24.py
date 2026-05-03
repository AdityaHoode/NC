# R1
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums=set(nums)
        res=0
        i=0
        while i<len(nums):
            if nums[i]-1 not in set_nums:
                length=1
                n=nums[i]
                while n+1 in set_nums:
                    length+=1
                    n+=1
                res=max(res,length)
            i+=1
        return res