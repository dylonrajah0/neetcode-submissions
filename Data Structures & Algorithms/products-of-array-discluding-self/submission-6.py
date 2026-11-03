class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #create arrays
        res = [0] * len(nums)
        pre =[0] * len(nums)
        suff = [0] * len(nums)

        #populate pre and suff
        pre[0] = 1
        for i in range(1, len(nums)):
            pre[i] = nums[i-1] * pre[i-1]

        suff[len(nums)-1] = 1
        for i in range(len(nums)-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]

        for i in range(0, len(res)):
            res[i] = pre[i] * suff[i]

        return res