from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen=Counter([t for t in board[i] if t!='.'])
            if seen.total()>0 and seen.most_common(1)[0][1]>1:
                return False

        for i in range(len(board)):
            temp=[]
            for j in range(len(board)):
                if board[j][i]!='.':
                    temp.append(board[j][i])
            seen=Counter(temp)
            if seen.total()>0 and seen.most_common(1)[0][1]>1:
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                temp = []
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if board[i][j] != '.':
                            temp.append(board[i][j])
                
                seen = Counter(temp)
                if seen and seen.most_common(1)[0][1] > 1:
                    return False        
        
        return True