class Solution:
    def trap(self, height: List[int]) -> int:
        res1=[0]
        res2=[0]
        prefix=0
        for i in range(1,len(height)):
            prefix=max(prefix,height[i-1])
            res1.append(prefix)
        print(res1)
        suffix=0
        for i in range(len(height)-2,-1,-1):
            suffix=max(suffix,height[i+1])
            res2.append(suffix)
        res2.reverse()
        print(res2)
        res3=0
        for i in range(len(height)):
            temp=min(res1[i],res2[i])-height[i]
            if temp>0:
                res3+=temp
        return res3