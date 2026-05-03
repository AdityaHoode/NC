# R1
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen=set()
        col_seen=set()
        box=defaultdict(set)
        for i in range(9):
            for j in range(9):
                val_row = board[i][j]
                if val_row != '.':
                    if val_row in row_seen:
                        return False
                    row_seen.add(val_row)

                val_col = board[j][i]
                if val_col != '.':
                    if val_col in col_seen:
                        return False
                    col_seen.add(val_col)
                box_id=(i//3,j//3)
                if val_row!='.':
                    if val_row in box[box_id]:
                        return False
                    box[box_id].add(val_row)
                    
            row_seen=set()
            col_seen=set()

        return True