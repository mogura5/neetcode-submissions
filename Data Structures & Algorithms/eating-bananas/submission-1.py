class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowest = 1
        highest = max(piles)
        res = highest

        
        while lowest <= highest:

            mid = lowest + ((highest - lowest) // 2)
            time = 0

            for p in piles:

                time += math.ceil(float(p) / mid)

            if time > h:

                lowest = mid + 1
            else:
                highest = mid - 1

                res = min(res, mid)
        return res

