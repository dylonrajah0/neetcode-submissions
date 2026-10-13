class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 0
        res = 0

        for left in range(0,len(prices)):
            for right in range(left+1, len(prices)):

                res = max(res, prices[right] - prices[left])

        
        return res

