class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk=[]
        res=0
        ps_list=sorted([(p,s) for p,s in zip(position,speed)], reverse=True)
        for p,s in ps_list:
            t=(target-p)/s
            if stk and stk[-1]<t:
                res+=1
                stk=[]
            elif stk and stk[-1]>t:
                continue
            stk.append(t)

        return res+1 if stk else res