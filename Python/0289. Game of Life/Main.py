class Solution:
    def gameOfLife(self, board):
        if board == [[]]: return
        row = len(board)
        col = len(board[0])

        nest  = [[0 for j in range(col +2)] for i in range(row+2)]
        big  = [[0 for j in range(col +2)] for i in range(row+2)]
        for i in range(1, row + 1):
            for j in range (1, col + 1):
                big[i][j] = board[i-1][j-1]

        for i in range(1, row + 1):
            for j in range (1, col + 1):
                neighbours = 0
                for x in range(-1,2):
                    for y in range (-1,2):
                        neighbours += big[i+x][y+j]
                neighbours -= big[i][j]  #计算邻居不用加入自己
                if big[i][j] == 1 and neighbours <2:
                    nest[i][j] = 0
                elif big[i][j] == 1 and neighbours >3:
                    nest[i][j] = 0
                elif big[i][j] == 0 and neighbours == 3:
                    nest[i][j] = 1
                else: 
                    nest[i][j] = big[i][j]

        for i in range(0 , row):
            for j in range (0, col):
                board[i][j] = nest[i+1][j+1]
               
if __name__ == "__main__":
    s = Solution()
    nums = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    s.gameOfLife(nums)   
    print(nums)    
        

        
