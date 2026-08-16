class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows    = defaultdict(list)
        columns = defaultdict(list)
        squares = defaultdict(list)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] 
                    or board[r][c] in columns[c] 
                    or board[r][c] in squares[(r//3,c//3)]):
                    return False
                rows[r].append(board[r][c])
                columns[c].append(board[r][c])
                squares[(r//3,c//3)].append(board[r][c])
                #print(squares)
        return True

        