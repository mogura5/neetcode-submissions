class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = -1
        output = [-1] * len(arr)

        for n in range(len(arr) - 1, -1, -1):

            output[n] = current_max

            current_max = max(current_max, arr[n])

        return output

        