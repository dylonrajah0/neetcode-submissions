class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        print("Nums: ",nums)
        size = len(nums)
        nums.extend(nums)
        print(nums)
        return nums