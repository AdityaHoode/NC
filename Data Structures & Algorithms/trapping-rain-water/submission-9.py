class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        s=[]
        for i,h in enumerate(height):
            while s and s[-1][1]<h:
                bottom=s.pop()
                if len(s)!=0:
                    cwidth=(i-s[-1][0])-1
                    cheight=min(h,s[-1][1])-bottom[1]
                    res+=max(cwidth*cheight,0)
            s.append((i,h))
        return res 