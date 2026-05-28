class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_seen = {}
        for i in range(9):
            row_seen = set()
            col_seen = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_seen:
                        return False
                    row_seen.add(board[i][j])
                
                if board[j][i] != ".":
                    if board[j][i] in col_seen:
                        return False
                    col_seen.add(board[j][i])
                
                if board[i][j] != ".":
                    box_key = (i//3, j//3)
                    if box_key not in box_seen:
                        box_seen[box_key] = set()
                    if board[i][j] in box_seen[box_key]:
                        return False
                    box_seen[box_key].add(board[i][j])
        
        return True       