class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        if s is None:
            return True
        if len(s) == 1:
            return False

        for i in s:
            
            if i == "(":
                stack.append(i)
            elif i == "{":
                stack.append(i)
            elif i == "[":
                stack.append(i)
            
            elif i == "}":
                if stack:
                    char = stack.pop()
                    if char != "{":
                        return False
                else:
                    return False
            elif i == "]":
                if stack:
                    char = stack.pop()
                    if char != "[":
                        return False
                else:
                    return False
            elif i == ")":
                if stack:
                    char = stack.pop()
                    if char != "(":
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True
            
            



