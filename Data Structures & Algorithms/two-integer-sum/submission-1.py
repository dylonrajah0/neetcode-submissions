class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}

        for index, value in enumerate(nums):
            print(index, value)

            if value in myMap:
                return [myMap[value], index]
            else:
                myMap[target - value] = index

        return [-1,-1]