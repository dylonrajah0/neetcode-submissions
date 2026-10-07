class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(0, len(board)):
            rowset = set()
            for col in range(0, len(board[0])):
                if board[row][col] != "." and board[row][col] in rowset:
                    return False

                rowset.add(board[row][col])

        for col in range(0, len(board[0])):
            colset = set()
            for row in range(0, len(board)):
                if board[row][col] != "." and board[row][col] in colset:
                    return False

                colset.add(board[row][col])

        for row in range(0,9,3):
            
            for col in range(0,9,3):

                gridSet = set()

                for r in range(row, row+3):
                    for c in range(col, col+3):

                        if board[r][c] != "." and board[r][c] in gridSet:
                            return False

                        gridSet.add(board[r][c])

        return True