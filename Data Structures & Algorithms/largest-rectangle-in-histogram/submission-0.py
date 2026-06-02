class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        areaStack = []

        for i, h in enumerate(heights):

            start = i
            while areaStack and areaStack[-1][1] > h:
                index, height = areaStack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            areaStack.append((start, h))
        for i, h in areaStack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


        