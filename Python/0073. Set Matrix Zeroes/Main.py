class Solution:
    def setZeroes(self, matrix):
        if not matrix:
            return []
        rowlst = []
        collst = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowlst.append(i)
                    collst.append(j)
        
        for i in rowlst:
            matrix[i] = [0] * len(matrix[0])
        for i in collst:
            for j in range(len(matrix)):
                matrix[j][i] = 0

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    s.setZeroes(matrix)
    print(matrix)
