class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        top, left = 0, 0
        right = len(matrix[0]) -1
        bottom = len(matrix) -1
        res = []
        while (True):
            for i in range(left, right+1):
                res.append(matrix[top][i])
                
            top += 1
            if top > bottom: break

            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1
            if left > right: break

            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom -=1
            if bottom < top: break
            
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
                
            left += 1
            if left > right:break
            
        return res
            



if __name__ == "__main__":
    s = Solution()
    res = s.spiralOrder([[2,5,8],[4,0,-1]])
    print(res)