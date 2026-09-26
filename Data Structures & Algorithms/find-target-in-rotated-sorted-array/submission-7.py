class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Obvious solution: Loop through the array, find the value
            #Runtime: O(n)
        #More Optimal -> Binary search
        #set left bound to 0, right bound to end
        #Calculate the pivot
        #One half of the array will be sorted, determine if its the left or right side
        #check if target is in the sorted half, if not search the other side (unsorted due to rotation)

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            print(mid)

            if nums[mid] == target:
                return mid

            #Check if left is sorted
            if nums[left] <= nums[mid]:
                #If true, check if target is in left side
                if nums[left] <= target < nums[mid]:
                    right = mid-1

                #target is in the right side
                else:
                    left = mid+1
            else:
                #right half must be sorted
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1


        return -1

