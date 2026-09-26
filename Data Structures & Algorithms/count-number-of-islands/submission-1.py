class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #traverse the matrix
        #When we see a 1, that represents an island.
        #call DFS on that number/island/position
        #Search for adjacent positions with "1" - not diagonals
        #Once there this no more adjacent 1's, increment the island count

        islandCount = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    self.dfs(grid, row, col)
                    islandCount += 1

        return islandCount

    def dfs(self, grid:list[List[str]], row: int, col: int):

        #make the current position 0 so position is counted multiple times
        grid[row][col] = "0"

        #check bounds and value of adjacent traversals

        if row-1 >= 0 and grid[row-1][col] == "1":
            self.dfs(grid, row-1, col)

        if row+1 < len(grid) and grid[row+1][col] == "1":
            self.dfs(grid, row+1, col)
        
        if  col+1 < len(grid[0]) and grid[row][col+1] == "1":
            self.dfs(grid, row, col+1)

        if  col-1 >= 0 and grid[row][col-1] == "1":
            self.dfs(grid, row, col-1)

