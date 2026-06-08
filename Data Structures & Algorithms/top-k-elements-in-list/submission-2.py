class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        if k == len(nums):
            return nums

        for val in nums:
            print(val)
            hashmap[val] = hashmap.get(val,0) + 1
       
        sorted_items = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)

        ret = []

        for i in range(k):
            ret.append(sorted_items[i][0])

        return ret