class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        print("Target: ", target)
        while(left <= right):
            print("in Loop")
            print("Left: ", left)
            print("Right: ", right)

            mid = (left + right) // 2

            print("Mid: ", mid)

            if target > nums[mid]:
                left = mid+1
                print("New Left: ", left)
            elif target < nums[mid]:
                right = mid-1
                print("New Right: ", right)
            else:   
                return mid


        return -1;