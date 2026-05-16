class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d=dict(sorted({p:s for p,s in zip(position,speed)}.items(), reverse=True))
        p=list(d.keys())
        s=list(d.values())
        stk=[]
        for i in range(len(p)):
            time=(target-p[i])/s[i]
            if stk and time<=stk[-1]:
                continue
            else:
                stk.append(time)
        return len(stk)