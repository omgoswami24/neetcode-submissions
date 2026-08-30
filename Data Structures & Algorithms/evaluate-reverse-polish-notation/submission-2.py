class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stk = []

        for val in tokens:
            if val == "+":
                a = int(stk.pop())
                b = int(stk.pop())

                stk.append(b + a)

            elif val == "-":
                a = int(stk.pop())
                b = int(stk.pop())

                stk.append(b - a)

            elif val == "*":
                a = int(stk.pop())
                b = int(stk.pop())

                stk.append(b * a)

            elif val == "/":
                a = int(stk.pop())
                b = int(stk.pop())

                stk.append(b / a)

            else:
                stk.append(int(val))
        
        return int(stk[0])

            
                


        
            
        