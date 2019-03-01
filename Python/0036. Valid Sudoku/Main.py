class Solution:
    def isValidSudoku(self, board):
        for i in range(len(board)):
            a = {}
            b = {}
            c = {}
            for j in range(len(board[0])):
                if board[i][j] in a and board[i][j]!='.':
                    return False
                else:
                    a[board[i][j]] = 1
                if board[j][i] in b and board[j][i]!='.':
                    return False
                else:
                    b[board[j][i]] = 1
                
                rowIndex = 3 * (i // 3)
                colIndex = 3 * (i % 3)
                tmp = board[rowIndex + j//3][colIndex + j%3]

                if tmp in c and tmp !='.':
                    return False
                else:
                    c[tmp] = 1
        return True


