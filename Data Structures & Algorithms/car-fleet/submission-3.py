class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        timeStack = []
        counter = 0

        for i, val in enumerate(position):
            stack.append([val, speed[i]])

        stack.sort(reverse = True)

        for p, s in stack:

            time = (target - p)/ s

            if timeStack and time <= timeStack[-1]:
                continue
            else:
                timeStack.append(time)

        
        return len(timeStack)