class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        rowCount = 0
        colCount = 0
        for i in range(9):
            rows.clear()
            rowCount = 0
            cols.clear()
            colCount = 0
            for j in range(9):
                if board[i][j] != ".":
                    rowCount += 1
                    rows.add(board[i][j])
                if board[j][i] != ".":
                    colCount += 1
                    cols.add(board[j][i])
            if ((len(rows) != rowCount) or (len(cols) != colCount)):
                return False
        squares = set()
        squareCount = 0
        for i in range(3):
            for j in range(3):
                squares.clear()
                squareCount = 0
                for k in range(9):
                    if board[(i * 3) + k // 3][(j * 3) + k % 3] != ".":
                        squareCount += 1
                        squares.add(board[(i * 3) + k // 3][(j * 3) + k % 3])
                if (len(squares) != squareCount):
                    return False
        return True