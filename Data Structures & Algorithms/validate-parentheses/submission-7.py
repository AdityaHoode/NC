class Solution:
    def isValid(self, s: str) -> bool:
        l=[c for c in s]
        stk=[]
        d={
            ')':'(',
            '}':'{',
            ']':'['
        }
        for x in l:
            if x in d.values():
                stk.append(x)
            else:
                if stk and d.get(x, None)==stk[-1]:
                    stk.pop()
                else:
                    return False
        return len(stk)==0   