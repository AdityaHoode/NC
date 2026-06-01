# R1
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res=0
        fleet_time=0
        for p,s in sorted([(p,s) for p,s in zip(position,speed)], reverse=True):
            t=(target-p)/s
            if t>fleet_time:
                res+=1
                fleet_time=t
        return res