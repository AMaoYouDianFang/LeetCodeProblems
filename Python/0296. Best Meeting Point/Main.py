#https://stackoverflow.com/questions/10402087/algorithm-for-minimum-manhattan-distance
class Solution(object):
    def minTotalDistance(self, grid):
        row = []
        col = []
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row.append(i)
                    col.append(j)
        print(col, row)
        col.sort() #无序的
        #row.sort() #有序的
        for i in row: 
            res += abs(row[len(row)//2] - i)
        for j in col:
            res += abs(col[len(col)//2] - j)
        return res


if __name__ == "__main__":
    s = Solution()
    grid = [[1,0,0,0,1], [0,0,0,0,0], [0,0,1,0,0]]
    res = s.minTotalDistance(grid)
    print(res)
        
# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0