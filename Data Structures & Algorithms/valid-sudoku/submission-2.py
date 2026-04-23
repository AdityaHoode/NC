from collections import Counter, defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=set()
        cols=set()
        boxes=defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val!='.' and val in rows:
                    return False
                rows.add(val)

                val = board[j][i]
                if val!='.' and val in cols:
                    return False
                cols.add(val)

                box_id = (i//3,j//3)
                val = board[i][j]
                if val!='.' and val in boxes[box_id]:
                    return False
                boxes[box_id].add(val)
            rows=set()
            cols=set()
        return True