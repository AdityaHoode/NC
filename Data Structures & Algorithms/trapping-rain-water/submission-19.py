# R1 - Two Pointer
class Solution:
    def trap(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        lmax,rmax=height[i],height[j]
        area=0
        while i<j:
            if lmax<=rmax:
                i+=1
                area+=max(0, lmax-height[i])
                lmax=max(lmax,height[i])
            else:
                j-=1            
                area+=max(0, rmax-height[j])
                rmax=max(rmax,height[j])
        return area