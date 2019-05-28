from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rowlist = [False] * m
        collist = [False] * n 
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rowlist[i] = True
                    collist[j] = True
        for i in range(m):
            for j in range(n):
                if rowlist[i] == True or collist[j] == True:
                    matrix[i][j] = 0

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    s.setZeroes(matrix)
    print(matrix)
