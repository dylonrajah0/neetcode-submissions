class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqCount = {}
        for num in nums:
            freqCount[num] = freqCount.get(num, 0)+1


        print(freqCount)
        print(len(nums))
        freq = [[] for _ in range(len(nums) + 1)]
        print(freq)

        for key in freqCount:
            freq[freqCount[key]].append(key)

        print("Frequency List: ", freq)
        

        res = []

        for x in range(len(freq)-1,-1,-1):
            print(x)
            if freq[x] != 0:
                res.extend(freq[x])

        print(res)
        return res[:k]
        