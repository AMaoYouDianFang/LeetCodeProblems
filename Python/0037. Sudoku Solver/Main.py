class Solution:  #使用DFS
    def solveSudoku(self, board):
        if not board:
            return 
        self.slove(board)

    def isPointValid(self, board, x, y, c):
        for i in range(9):
            if board[i][y] == c: # check col
                return False
            if board[x][i] == c: # check row
                return False
            if board[3*(x//3)+i//3][3*(y//3)+i%3] == c: # check 3 * 3 block
                return False
        return True
    def slove(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in '123456789':
                        if self.isPointValid(board,i,j,c):
                            board[i][j] = c
                            if self.slove(board): 
                                return True
                            else:
                                board[i][j] = '.' #返回上一层，因为有可能当的数导致后面的数不行
                    return False
        return True

    