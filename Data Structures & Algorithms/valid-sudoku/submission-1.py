class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #check all rows
        for row in range(len(board)):
            rowSet = set()
            for col in range(len(board[0])):
                #print(board[row][col])
                if(board[row][col] in rowSet):
                    print("returning False 1")
                    return False

                if (board[row][col] != "."):
                    rowSet.add(board[row][col])

        #check all columns
        for col in range(len(board[0])):
            print("next column")
            colSet = set()
            for row in range(len(board)):
                
                if(board[row][col] in colSet):
                    print("returning False 2")
                    return False

                if(board[row][col] != "."):
                    print("number: ", board[row][col])
                    colSet.add(board[row][col])
                    print(colSet)

        #check the 3x3 grids
        for boxRow in range(0,len(board),3):
            for boxCol in range(0,len(board[0]),3):
                #print("In inner loop")
                gridSet = set()
                for row in range(boxRow, boxRow+3):
                    for col in range(boxCol, boxCol+3):
                        #print(board[row][col])
                        if board[row][col] in gridSet:
                            #print("returning False 3")
                            return False

                        if(board[row][col] != "."):
                            #print("Adding number to set", board[row][col])
                            gridSet.add(board[row][col])
                            #print(gridSet)
                    

        return True