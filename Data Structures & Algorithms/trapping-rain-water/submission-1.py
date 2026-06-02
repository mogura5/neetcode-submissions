class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        maxArea = 0
        leftMax = height[left]
        rightMax = height[right]
        if not height:
            return 0

        while left < right:

            if leftMax < rightMax:

                left += 1
                leftMax = max(leftMax, height[left])
                maxArea += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                maxArea += rightMax - height[right]
            
        return maxArea
