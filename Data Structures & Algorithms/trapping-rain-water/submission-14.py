# R1
class Solution:
    def trap(self, height: List[int]) -> int:
        stk=[]
        area=0
        for i,h in enumerate(height):
            start_index=i
            while stk and stk[-1][1]<h:
                bottom=stk.pop()
                if len(stk)!=0:
                    width=i-stk[-1][0]-1
                    height=min(stk[-1][1], h)-bottom[1]
                    area+=height*width
            stk.append((start_index,h))    
        return area                                           