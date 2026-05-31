# R1
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        res=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stk and t>stk[-1][1]:
                prev_day,prev_temp=stk.pop()
                res[prev_day]=(i-prev_day)
            stk.append((i,t))
        return res