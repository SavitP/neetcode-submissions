class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count+=1
                    grid = self.explore(grid, i, j)
        return count
    
    def explore(self, grid: List[List[str]], row, col):
        grid[row][col] = "0"
        if len(grid) - 1 >= row + 1 and grid[row+1][col] == "1":
            grid = self.explore(grid, row+1, col)
        if len(grid[0]) - 1 >= col + 1 and grid[row][col+1] == "1":
            grid = self.explore(grid, row, col+1)
        if row - 1 >= 0 and grid[row-1][col] == "1":
            grid = self.explore(grid, row-1, col)
        if col-1 >= 0 and grid[row][col-1] == "1":
            grid = self.explore(grid, row, col-1)
        return grid
