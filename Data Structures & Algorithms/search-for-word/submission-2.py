class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = set()
        self.found = False
        def find(x, y, s):
            used.add((x, y))
            if s == "":
                self.found = True
                return
            if x > 0 and board[y][x - 1] == s[:1] and (x - 1,y) not in used:
                find(x - 1, y, s[1:])
                used.remove((x - 1, y))
                if self.found:
                    return
            if y > 0 and board[y - 1][x] == s[:1] and (x,y - 1) not in used:
                find(x, y - 1, s[1:])
                used.remove((x, y - 1))
                if self.found:
                    return
            if x < len(board[0]) - 1 and board[y][x + 1] == s[:1] and (x + 1,y) not in used:
                find(x + 1, y, s[1:])
                used.remove((x + 1, y))
                if self.found:
                    return
            if y < len(board) - 1 and board[y + 1][x] == s[:1] and (x,y + 1) not in used:
                find(x, y + 1, s[1:])
                used.remove((x, y + 1))
                if self.found:
                    return

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[:1]:
                    find(j, i, word[1:])
                    if self.found:
                        return True
                    used.remove((j, i))
        return False