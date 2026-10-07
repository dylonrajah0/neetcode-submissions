class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #1 Create 3 arrays 
        pref = [0] * len(nums)
        suff = [0] * len(nums)
        res =  [0] * len(nums)

        #2 Set the ends
        pref[0] = 1
        suff[len(suff) -1] = 1

        #3 Build the arrays

        for i in range(1, len(nums)):
            pref[i] = nums[i-1] * pref[i-1]


        for i in range(len(nums) - 2, -1, -1):
            suff[i] = nums[i+1] * suff[i+1]


        for i in range(0, len(nums)):
            res[i] = pref[i] * suff[i]

        return res