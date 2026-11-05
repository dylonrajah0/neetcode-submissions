class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh = 0

        queue = deque()

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):

                if grid[row][col] == 2:
                    coor = [row,col]
                    queue.append(coor)
                
                if grid[row][col] == 1:
                    fresh += 1

        minute = 0
        while queue and fresh > 0:

            size = len(queue)

            for i in range(0, size):
                curr = queue.popleft()

                row = curr[0]
                col = curr[1]

                if (row-1 >= 0 and grid[row-1][col] == 1):
                    grid[row-1][col] = 2
                    queue.append([row-1,col])
                    fresh -= 1
                
                if (row+1 < len(grid) and grid[row+1][col] == 1):
                    grid[row+1][col] = 2
                    queue.append([row+1, col])
                    fresh -= 1
                
                if (col-1 >= 0 and grid[row][col-1] == 1):
                    grid[row][col-1] = 2
                    queue.append([row, col-1])
                    fresh -= 1

                if (col+1 < len(grid[0]) and grid[row][col+1] == 1):
                    grid[row][col+1] = 2
                    queue.append([row, col+1])
                    queue.append([row, col+1])
                    fresh -= 1

            minute += 1




        if fresh > 0:
            return -1

        return minute
