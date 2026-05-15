class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        res=[0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stk and t>stk[-1][1]:
                lower_temp=stk[-1][1]
                lower_temp_index=stk[-1][0]
                res[lower_temp_index]=i-lower_temp_index
                stk.pop()
            stk.append((i,t))
        return res
