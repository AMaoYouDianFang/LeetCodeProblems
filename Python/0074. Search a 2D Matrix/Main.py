#2-10
class Solution:
    def searchMatrix(self, matrix, target):
        if matrix:
            return False
        for i in matrix:
            if target <= i[-1]:
                if target in i:
                    return True
                else:
                    return False
        return False

    #二分法查找，两次二分法，第一次查找矩阵的第一列，第二次查找对应的行的位置
    def searchMatrix1(self, matrix, target):
        if matrix is None or matrix[0] is None:
        #if matrix == [] or matrix == [[]]: #!!! 没有考虑 行的元素不能为空，列的因为不能为空
            return False
        l, r = 0, len(matrix)-1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] == target: return True
            elif matrix[mid][0] < target : l = mid + 1
            else: r = mid - 1
        row = l - 1 #!!!第一次写错了
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target: return True
            elif matrix[row][mid] < target : l = mid + 1
            else: r = mid - 1
        return False

    #一次二分查找
    def searchMatrix2(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        s = 0
        e = n*m-1
        while s <= e:
            mid = (s+ e) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col]  > target:
                e = mid - 1
            else:
                s = mid + 1
        return False
#注意[[]]
if __name__ == "__main__":
    s =Solution()
    res = s.searchMatrix1([], 0)
    print()
