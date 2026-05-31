# R1
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        res=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stk and t>temperatures[stk[-1]]:
                prev_day=stk.pop()
                res[prev_day]=i-prev_day
            stk.append(i)
        return res