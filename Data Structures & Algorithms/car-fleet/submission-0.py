class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [0] * len(position)
        counter = 0
        timeStack = []
        for i, val in enumerate(position):
            stack[i] = [val, speed[i]]
        stack.sort(reverse=True)

        for p, s in stack:

                time = ((target - p)/s)
                timeStack.append(time)

                if len(timeStack) >= 2 and timeStack[-1] <= timeStack[-2]:
                    timeStack.pop()
        return len(timeStack)