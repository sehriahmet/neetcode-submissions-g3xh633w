class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minValue = 1
        maxValue = max(piles)
        result = maxValue

        while minValue <= maxValue: 
            mid = (minValue + maxValue) // 2

            time = 0

            for i in piles:
                time += math.ceil(i/mid)
            
            if time <= h:
                result = mid
                maxValue = mid - 1
            else:
                minValue = mid + 1

        return result 
