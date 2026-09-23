from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[len(grid) - 1][len(grid) - 1] == 1:
            return -1
        if len(grid) == 1:
            return 1
        visited = {(0, 0)}
        q = deque()
        q.append((0, 0, 1))
        while len(q) > 0:
            row, col, step = q.popleft()
            if row > 0 and grid[row - 1][col] == 0 and (row - 1, col) not in visited:
                visited.add((row - 1, col))
                q.append((row - 1, col, step + 1))
            if col > 0 and grid[row][col - 1] == 0 and (row, col - 1) not in visited:
                visited.add((row, col - 1))
                q.append((row, col - 1, step + 1))
            if row > 0 and col > 0 and grid[row - 1][col - 1] == 0 and (row - 1, col - 1) not in visited:
                visited.add((row - 1, col - 1))
                q.append((row - 1, col - 1, step + 1))
            if row > 0 and col < len(grid) - 1 and grid[row - 1][col + 1] == 0 and (row - 1, col + 1) not in visited:
                visited.add((row - 1, col + 1))
                q.append((row - 1, col + 1, step + 1))
            if row < len(grid) - 1 and col > 0 and grid[row + 1][col - 1] == 0 and (row + 1, col - 1) not in visited:
                visited.add((row + 1, col - 1))
                q.append((row + 1, col - 1, step + 1))
            if row < len(grid) - 1 and grid[row + 1][col] == 0 and (row + 1, col) not in visited:
                if row + 1 == len(grid) - 1 and col == len(grid) - 1:
                    return step + 1
                visited.add((row + 1, col))
                q.append((row + 1, col, step + 1))
            if col < len(grid) - 1 and grid[row][col + 1] == 0 and (row, col + 1) not in visited:
                if col + 1 == len(grid) - 1 and row == len(grid) - 1:
                    return step + 1
                visited.add((row, col + 1))
                q.append((row, col + 1, step + 1))
            if row < len(grid) - 1 and col < len(grid) - 1 and grid[row + 1][col + 1] == 0 and (row + 1, col + 1) not in visited:
                if row + 1 == len(grid) - 1 and col + 1 == len(grid) - 1:
                    return step + 1
                visited.add((row + 1, col + 1))
                q.append((row + 1, col + 1, step + 1))

        return -1

