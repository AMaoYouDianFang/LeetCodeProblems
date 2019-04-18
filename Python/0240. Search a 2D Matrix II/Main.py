#2-10
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        x = len(matrix) -1 
        y = 0
        while True:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                x -= 1
            else: 
                y += 1
            if x < 0 or y >= len(matrix[0]):
                break
        return False

        