class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    #Return all triplets that sum to 0
    # NO duplicates
    #can return in any order

    #Approach 2sum with outer pivot
    #[-1,0,1,2,-1,-4], if we are at -1, we need to find 2 values that sum to 1
    #Loop needs to go from start to 0 to len(nums)-3

    #Time Complexity: O(n^2)
    
        nums.sort()

        retList = []
        for i in range(0, len(nums)-2):
            #if the first number is the same as the number we just processed, skip (duplicate)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            firstNum = nums[i]

            left =i+1
            right = len(nums)-1

            #search for -firstNum
            while (left < right):
                if nums[left] + nums[right] == -firstNum:
                    #append to list
                    retList.append([firstNum, nums[left], nums[right]])
                    #check for others, check for duplicates
                    left +=1 
                    right -= 1

                    #when we move left, make sure the next number isnt a duplicate
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                    #when we move left, make sure the next number isnt a duplicate
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                    
                
                elif nums[left] + nums[right] < -firstNum:
                    left += 1

                else:
                    right -= 1

        return retList


