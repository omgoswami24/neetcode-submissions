class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for item in s:
            if item == "(" or item == "[" or item == "{":
                stk.append(item)
            else:
                if item == ")":
                    if len(stk) <= 0:
                        return False
                    x = stk.pop()
                    if x != "(":
                        return False
                
                elif item == "]":
                    if len(stk) <= 0:
                        return False
                    x = stk.pop()
                    if x != "[":
                        return False

                elif item == "}":
                    if len(stk) <= 0:
                        return False
                    x = stk.pop()
                    if x != "{":
                        return False
        if len(stk) > 0:
            return False
        return True
                        