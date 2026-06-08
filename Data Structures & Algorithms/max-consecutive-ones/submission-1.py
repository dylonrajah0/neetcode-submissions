class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxCount = 0
        currCount = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                print("Found a 1")
                currCount += 1
            else:
                print("Found a 0")
                print("currCount: ", currCount)
                maxCount = max(maxCount, currCount)
                print("Max Count: ", maxCount)
                currCount = 0
        maxCount = max(maxCount, currCount)
        print(maxCount)
        return maxCount