class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        res=1
        op=[]
        n = sorted(set(nums))
        for i in range(len(n)-1):
            if n[i]+1-n[i+1] == 0:
                res+=1
            else:
                op.append(res)
                res=1
        op.append(res)
        print(op)
        return res if op==[] else sorted(op, reverse=True)[0]