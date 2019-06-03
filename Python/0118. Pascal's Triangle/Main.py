class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1: return []
        res = []
        for i in range(numRows):
            lst = [1] * (i+1)
            if i > 1:
                for j in range(1, i):
                    lst[j] = res[-1][j] + res[-1][j-1]
            res.append(lst)
        return res