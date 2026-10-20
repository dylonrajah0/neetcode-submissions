class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        #binary search the rows

        bottom = 0
        top = len(matrix)-1

        while bottom <= top:
            mid = (bottom + top) // 2

            if target < matrix[mid][0]:
                top = mid -1
            elif target > matrix[mid][-1]:
                bottom = mid + 1
            else:
                row = mid
                break
        else:
            return False

        left = 0
        right = len(matrix[row])-1

        while left <= right:

            mid = (left + right) // 2

            if target < matrix[row][mid]:
                right = mid-1
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                col = mid
                break
        else:
            return False
        
        return True