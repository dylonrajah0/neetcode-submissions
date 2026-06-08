class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maxRight = -1
        for i in range(len(arr)-1, -1, -1):
            oldValue = arr[i]
            print("old value: ", oldValue)
            arr[i] = maxRight
            print("Curr Array: ",arr)
            maxRight = max(maxRight, oldValue)
            print("maxRight: ", maxRight)

     


        return arr
