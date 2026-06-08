class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        overwriteIndex = 0

        for i in range(len(nums)):

            if(nums[i] != val):
                nums[overwriteIndex] = nums[i]
                overwriteIndex += 1

        return overwriteIndex

        