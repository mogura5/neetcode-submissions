class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom:
            mid = top + ((bottom - top) // 2)

            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                break
        if not (top <= bottom):
            return False
        while left <= right:
            colMid = left + ((right - left) // 2)
            if matrix[mid][colMid] < target:
                left = colMid + 1
            elif matrix[mid][colMid] > target:
                right = colMid - 1
            else:
                return True
        return False



            