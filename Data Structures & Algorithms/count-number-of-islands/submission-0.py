class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (grid[r][c] == '1'):
                    count +=1 
                    self.dfs(grid, r, c)

        return count


    def dfs(self, grid: List[List[str]], r: int, c: int):

        ROW = len(grid)
        COL = len(grid[0])

        if (min(r,c) < 0 or
            r == ROW or c == COL or
            grid[r][c] == '0'):
            return

        grid[r][c] = '0'

        self.dfs(grid, r+1, c)
        self.dfs(grid, r-1, c)
        self.dfs(grid, r, c-1)
        self.dfs(grid, r, c+1)



