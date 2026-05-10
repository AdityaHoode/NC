class Solution:
    def trap(self, height: List[int]) -> int:
        res=[0]
        prefix=0
        for i in range(1,len(height)):
            prefix=max(prefix,height[i-1])
            res.append(prefix)
        suffix=0
        for i in range(len(height)-2,-1,-1):
            suffix=max(suffix,height[i+1])
            res[i+1]=min(res[i+1], suffix)-height[i+1]
        c=0
        for n in res:
            if n>0:
                c+=n
        return c