# R1 - Two Pointer
class Solution:
    def trap(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        lmax,rmax=height[i],height[j]
        area=0
        while i<j:
            if lmax<=rmax:
                area+=max(0, lmax-height[i])
                i+=1
                lmax=max(lmax,height[i])
            else:
                area+=max(0, rmax-height[j])
                j-=1            
                rmax=max(rmax,height[j])
        return area