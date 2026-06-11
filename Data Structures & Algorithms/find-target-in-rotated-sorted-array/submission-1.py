class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        smallest = sys.maxsize
        for num in nums:
            smallest = min(num, smallest)

       
        split = nums.index(smallest)
        print("Split: ", split)
        print("Left: ",nums[:split])
        print("Right: ", nums[split:])
        print("Target: ", target)
        left = self.binarySearch(0, split-1, nums, target)
        right = self.binarySearch(split, len(nums)-1 , nums, target)
        
        print("Left Binary Search: ",left)
        print("Right Binary Search: ",right)



        if left != -1:
            return left
        elif right != -1:
            return right
        else:
            return -1

    def binarySearch(self, left: int, right: int, nums: List[int], target: int) -> int:

   
        print("In binarySearch")

        print("Left: ", left)
        print("Right: ", right)

        while (left <= right):

            mid = (left+right) // 2
            #print("Mid: ", mid)

            #print("nums[left]: ", nums[left])
            #print("nums[right]: ", nums[right])

            if target > nums[mid]:
                left = mid+1
                #print("new left: ", left)
            elif target < nums[mid]:
                right = mid-1
                #print("new right: ", right)
            else:
                return mid

        return -1