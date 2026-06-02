class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        stack = []

        def backtracking(numO, numC):

            if numO == n and numC == n:
                result.append("".join(stack))
                return
            if numO < n:
                stack.append("(")
                backtracking(numO + 1, numC)
                stack.pop()
            
            if numO > numC:
                stack.append(")")
                backtracking(numO, numC + 1)
                stack.pop()

        backtracking(0, 0)
        return result