class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                size = self.dfs(grid, r, c)
                maxArea = max(maxArea, size)

        return maxArea


    def dfs(self, grid: List[List[int]], r: int, c: int) -> int:

        ROW = len(grid)
        COL = len(grid[0])

        if(min(r,c) < 0 or
           r >= ROW or c >= COL or
           grid[r][c] == 0):
           return 0

        if(grid[r][c] == 1):
            grid[r][c] = 0

        return (
            1
            + self.dfs(grid, r + 1, c)
            + self.dfs(grid, r - 1, c)
            + self.dfs(grid, r, c + 1)
            + self.dfs(grid, r, c - 1)
        )

        