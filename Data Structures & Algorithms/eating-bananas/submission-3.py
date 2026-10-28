class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)

        while left < right:

            k  = (left + right)//2

            hours_needed = 0

            for pile in piles:
                hours = pile // k

                if pile % k != 0:
                    hours += 1

                hours_needed += hours

            if hours_needed > h:
                left = k + 1
            else:
                right = k

        return left
            

