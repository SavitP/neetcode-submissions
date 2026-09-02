class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def explore(count, row, col):
            count += 1
            grid[row][col] = 0
            if row > 0 and grid[row - 1][col] == 1:
                count = explore(count, row - 1, col)
            if col > 0 and grid[row][col - 1] == 1:
                count = explore(count, row, col - 1)
            if row < len(grid) - 1 and grid[row + 1][col] == 1:
                count = explore(count, row + 1, col)
            if col < len(grid[row]) - 1 and grid[row][col + 1] == 1:
                count = explore(count, row, col + 1)
            return count
        
        max = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    size = explore(0, i, j)
                    if size > max:
                        max = size
        return max