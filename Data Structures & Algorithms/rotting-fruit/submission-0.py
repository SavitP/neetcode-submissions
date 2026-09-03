class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i, j))
        count = 0
        while len(q) > 0:
            found = False
            for i in range(len(q)):
                row, col = q.popleft()
                if grid[row][col] == 1:
                    grid[row][col] = 2
                    found = True
                if row > 0 and grid[row - 1][col] == 1:
                    q.append((row - 1, col))
                if col > 0 and grid[row][col - 1] == 1:
                    q.append((row, col - 1))
                if row < len(grid) - 1 and grid[row + 1][col] == 1:
                    q.append((row + 1, col))
                if col < len(grid[row]) - 1 and grid[row][col + 1] == 1:
                    q.append((row, col + 1))
            if found:
                count += 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        return count