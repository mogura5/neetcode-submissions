class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = max(piles)

        while left <= right:

            mid = left + ((right - left) // 2)
            time = 0

            for p in piles:

                time += math.ceil(p / mid)
            
            if time <= h:
                result = min(result, mid)
                right = mid - 1
            
            if time > h:
                left = mid + 1
        
        return result


