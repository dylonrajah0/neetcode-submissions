class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
      for i in range(len(arr)):
        maxValue = -1
        print("starting at: ", i)
        for j in range(i+1, len(arr)):
            maxValue = max(maxValue, arr[j])
            print("max value found: ", maxValue)


        arr[i] = maxValue
        print(arr)


      return arr
