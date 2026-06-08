class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        maxStreak = 0
        for num in nums:
            print("num: ", num)
            currStreak = 1
            if num-1 not in numSet:
                add = 1
                
                while num+add in numSet:
                    print("found this number in set: ", num+add)
                    currStreak += 1
                    add += 1

                print(currStreak)
            maxStreak = max(maxStreak,currStreak)

        return maxStreak
        