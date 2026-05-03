# R1
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        res=1
        temp=1
        l=sorted(set(nums))
        for i in range(len(l)):
            if l[i]-1 in l:
                temp+=1
            else:
                temp=1
            res=max(res,temp)
        return res # 0,1,2,3,4,5,6