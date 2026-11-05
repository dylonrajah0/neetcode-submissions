class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        numIslands = 0

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):

                if grid[row][col] == "1":
                    numIslands += 1
                    self.dfs(grid, row, col)

        return numIslands

    def dfs(self, grid: List[List[str]], row: int, col: int):

        grid[row][col] = "0"

        if (row-1 >= 0 and grid[row-1][col] == "1"):
            self.dfs(grid, row-1, col)
        if (row + 1 < len(grid) and grid[row+1][col] == "1"):
            self.dfs(grid, row+1, col)
        if (col-1 >= 0 and grid[row][col-1] == "1"):
            self.dfs(grid, row, col-1)
        if (col+1 < len(grid[0]) and grid[row][col+1] == "1"):
            self.dfs(grid, row, col+1)
