# R1
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk=[]
        area=0
        for i,h in enumerate(heights):
            prev_i=i
            while stk and h<stk[-1][1]:
                prev_i,prev_h=stk.pop()
                area=max(area,prev_h*(i-prev_i))
            stk.append((prev_i,h))
        h_len=len(heights)
        for i,h in stk:
            area=max(area,h*(h_len-i))
        return area