class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stk=[]
        for p,s in cars:
            time=(target-p)/s
            if stk and time<=stk[-1]:
                continue
            else:
                stk.append(time)
        return len(stk)