class Solution:
    def trap(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        res=0
        lmax,rmax=height[i],height[j]
        while i<j:
            if lmax<=rmax:
                i+=1
                res+=max(lmax-height[i],0)
                lmax=max(lmax,height[i])
            else:
                j-=1
                res+=max(rmax-height[j],0)
                rmax=max(rmax,height[j])
        return res