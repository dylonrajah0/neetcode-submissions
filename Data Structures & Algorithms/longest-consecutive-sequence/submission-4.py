class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0

        for num in nums:

            if num-1 not in numSet:

                add = 0
                currStreak = 0
                while num+add in numSet:
                    currStreak +=1
                    add += 1

                longest = max(longest, currStreak)

        return longest
