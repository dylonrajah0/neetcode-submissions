class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        split = self.findPivot(nums)
        print("Split: ", split)

        #determine if we need to search left side or right side of split
        res = 0
        if nums[split] <= target <= nums[len(nums)-1]:
            res = self.binarySearch(nums, target, split, len(nums)-1)
        else:
            res = self.binarySearch(nums, target, 0, split-1)

        
        print("Res: ", res)
        return res

    def findPivot(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) -1

        while (left < right):
            mid = (left + right) //2

            if nums[mid] > nums[right]:
                left = mid+1

            elif nums[mid] < nums[left]:
                right = mid
            else:
                return left
        
        return left

    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:

        while (left <= right):

            mid = (left+right)//2

            if nums[mid] > target:
                right = mid-1

            elif nums[mid] < target:
                left = mid+1
            else:
                return mid


        return -1