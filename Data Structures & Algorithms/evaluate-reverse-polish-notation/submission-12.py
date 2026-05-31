# R1
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        for op in tokens:
            if op in '+-*/':
                operator=op
                operand2=int(stk.pop())
                operand1=int(stk.pop())
                if operator=='+':
                    stk.append(operand1+operand2)
                elif operator=='-':
                    stk.append(operand1-operand2)
                elif operator=='*':
                    stk.append(operand1*operand2)
                else:
                    stk.append(int(operand1/operand2))
            else:
                stk.append(op)
        print(stk)
        return int(stk[-1])