# R1
class Solution:
    def isValid(self, s: str) -> bool:
        p_map={
            ')':'(',
            '}':'{',
            ']':'['
        }
        stk=[]
        for p in s:
            if p in '({[':
                stk.append(p)
            else:
                if stk and p_map.get(p) == stk[-1]:
                    stk.pop()
                else:
                    return False
        return len(stk)==0