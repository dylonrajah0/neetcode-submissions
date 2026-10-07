class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for number, count in hashmap.items():

            buckets[count].append(number)

        res = []

        for numList in range(len(buckets)-1, 0, -1):
            for num in buckets[numList]:
                res.append(num)
                if len(res) == k:
                    return res

        return []