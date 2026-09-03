class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))
        dist = 1
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    r, c = row + dr, col + dc
                    if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 2147483647:
                        grid[r][c] = dist
                        q.append((r, c))
            dist += 1