import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        for t in tokens:
            if t not in "+-*/":
                stk.append(t)
            else:
                op=t
                op2=int(stk.pop())
                op1=int(stk.pop())
                if op=='+':
                    stk.append(op1+op2)
                elif op=='-':
                    stk.append(op1-op2)
                elif op=='*':
                    stk.append(op1*op2)
                else:
                    q=op1/op2
                    q=math.floor(q) if q>=0 else math.ceil(q)
                    stk.append(q)
        return int(stk[-1])