class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        lowest = float('inf')

        for index,num in enumerate(prices):
            if num < lowest:
                high = 0
                lowest = num
                while index+1 < len(prices):
                    high = max(high,prices[index+1])
                    index +=1

                profit = max(profit, high-lowest)

        print(profit)
        return profit
            
           