class Solution:
    def rotate(self, matrix):
        l = len(matrix)
        matrix.reverse() #注意用法不能返回值 复杂度？？？ 也可以直接将矩阵上下反转
        
        for i in range(l):
            for j in range(i, l):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        return matrix

if __name__ == "__main__":
    s = Solution()
    res = s.rotate([[1,2,3],[4,5,6],[7,8,9]])
    #print (len([[1,2,3],[4,5,6],[7,8,9]]))
    print(res)       