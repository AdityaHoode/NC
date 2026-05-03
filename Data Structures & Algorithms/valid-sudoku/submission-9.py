# R1
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen=defaultdict(set)
        col_seen=defaultdict(set)
        box_seen=defaultdict(set)
        for i in range(9):
            for j in range(9):

                val=board[i][j]
                box_key=(i//3,j//3)

                if val!='.':
                    if val in row_seen[i] or val in col_seen[j] or val in box_seen[box_key]:
                        return False
                
                    row_seen[i].add(val)
                    col_seen[j].add(val)
                    box_seen[box_key].add(val)

        return True
