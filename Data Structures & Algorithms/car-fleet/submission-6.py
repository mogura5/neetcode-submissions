class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        cars.sort(reverse=True)
        timeStack = []

        for i, c in enumerate(cars):
            time = (target - c[0] ) / c[1]

            if not timeStack or timeStack[-1] < time:
                timeStack.append(time)

        return len(timeStack)


