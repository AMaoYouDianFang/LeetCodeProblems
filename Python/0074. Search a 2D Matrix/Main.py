class Solution:
    def searchMatrix(self, matrix, target):
        if matrix==[[]]:
            return False
        for i in matrix:
            if target <= i[-1]:
                if target in i:
                    return True
                else:
                    return False
        return False
#注意[[]]
if __name__ == "__main__":
    s =Solution()
    res = s.searchMatrix([[]], 0)
    print(res)
