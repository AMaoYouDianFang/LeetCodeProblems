class Solution:
    def numIslands(self, grid) -> int:
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])
        res = 0
        visit = [ [False] * n] *m
        for i in range(m):
            for j in range(n):
                print(i,j,visit[i][j])
                if grid[i][j] == '1' and visit[i][j] ==False:
                    
                    self.DFS(grid, visit, i,j)
                    res += 1
        return res
    def DFS (self, grid, visit, x, y):
        if x < 0 or x >= len(grid) : return 
        if y < 0 or y >= len(grid[0]): return 
        if grid[x][y] == '0' or visit[x][y] ==True: return 
        visit[x][y] = True
        print(x,y)
        self.DFS(grid, visit, x-1, y)
        self.DFS(grid, visit, x+1, y)
        self.DFS(grid, visit, x, y -1)
        self.DFS(grid, visit, x, y + 1)
        
        

if __name__ == "__main__":
    grid = [["0","1","0"],["1","0","1"],["0","1","0"]]
    s = Solution()
    res = s.numIslands(grid)
    print(res)