class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk=[]
        res=0
        fleet_time=0
        ps_list=sorted([(p,s) for p,s in zip(position,speed)], reverse=True)
        for p,s in ps_list:
            t=(target-p)/s
            if t>fleet_time:
                res+=1
                fleet_time=t
        return res