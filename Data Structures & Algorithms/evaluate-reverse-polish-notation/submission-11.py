class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:

            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(float(second) / first))
            elif t == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            else:
                stack.append(int(t))
        return stack[-1]