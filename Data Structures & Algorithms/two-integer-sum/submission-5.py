class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i in range(0, len(nums)):
            hashmap[nums[i]] = i

        for i in range(0, len(nums)):

            num = target - nums[i]

            if num in hashmap and hashmap[num] != i:
                return [i,hashmap[num]]

        return []