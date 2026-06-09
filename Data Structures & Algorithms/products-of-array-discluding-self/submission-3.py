class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # build left subarray
        # build the right subarray

        res = [0] * len(nums)
        #print("Res: ", res)

        for index in range(len(nums)):
            #print("Index: ", index)
            product = 1
            for x in range(len(nums)):
                
                if x != index:
                    #print("Multiplying by", nums[x])
                    product *= nums[x]
                    #print("Product: ", product)

            #print("Inserting at index: ", index)
            res[index] = product
            #print("Res: ", res)

            
        return res