class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}

        for num in nums:
            myMap[num] = myMap.get(num,0)+1

        freq = [[] for _ in range(len(nums)+1)]

        print(freq)

        for key, value in myMap.items():
            print(key)
            print(value)
            freq[value].append(key)

        arr = []

        for i in reversed(freq):
            print(i)
            if i:
                arr.extend(i)

            if len(arr) == k:
                break

        print(arr)
        return arr