class Solution:
    def trap(self, height: List[int]) -> int:
        area=0
        stk=[]
        for i,h in enumerate(height):
            start_index=i
            while stk and stk[-1][1]<h:
                bottom=stk.pop()
                if len(stk)!=0:
                    area+=(min(stk[-1][1],h)-bottom[1])*((i-stk[-1][0])-1)
            stk.append((start_index,h))
        print(stk)
        return area
