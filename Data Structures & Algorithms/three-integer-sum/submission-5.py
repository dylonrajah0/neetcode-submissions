class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        nums.sort()
        for i in range(0, len(nums)-2):

            #skip if its a duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue

            firstNum = nums[i]

            left = i+1
            right = len(nums)-1

            while left < right:

                if nums[left] + nums[right] == -firstNum:
                    currList = []
                    currList.append(firstNum)
                    currList.append(nums[left])
                    currList.append(nums[right])

                    res.append(currList)

                    left += 1
                    right -= 1

                    while left < len(nums)-1 and nums[left-1] == nums[left]:
                        left += 1

                    while right > 0 and nums[right+1] == nums[right]:
                        right -= 1

                elif nums[left] + nums[right] > -firstNum:
                    right -= 1

                else:
                    left += 1

        return res