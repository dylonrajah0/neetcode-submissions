class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        hashmap = {}
        for i in range(0, len(nums)):
            hashmap[nums[i]] = i

        print(hashmap)

        for i in range(0, len(nums)):
            difference = target - nums[i]

            if difference in hashmap and hashmap[difference] != i:
                return [i,hashmap[difference]]

        return []