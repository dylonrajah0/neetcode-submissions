class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #multiply before me * multiply after me
        # BRUTE FORCE

        arr = []

        for index, curr in enumerate(nums):
            #print("index", index)
            leftProd = 1
            rightProd = 1
            for left in range(index):
                
                leftProd *= nums[left]
                
            #print("leftProd", leftProd)
            for right in range(index+1, len(nums)):
                #print("right Index: ", right)
                
                rightProd *= nums[right]
                
            #print("rightProd", rightProd)
            prod = rightProd*leftProd
            #print("print", prod)
            arr.append(prod)
        #print(arr)
        return arr