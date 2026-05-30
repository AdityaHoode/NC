# R1 - Prefix & Suffix Arrays
class Solution:
    def trap(self, height: List[int]) -> int:
        res=[0]
        prefix_max=0
        for i in range(1,len(height)):
            prefix_max=max(prefix_max,height[i-1])
            res.append(prefix_max)
        suffix_max=0
        for j in range(len(height)-2,-1,-1):
            suffix_max=max(suffix_max,height[j+1])
            res[j+1]=max(min(res[j+1],suffix_max)-height[j+1],0)
        return sum(res)