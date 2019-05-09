from typing import List
class Solution:
    #Time: O(m*n), Space: O(m*n)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        d = [[None]* n for i in range(m)]

        d[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(1,m):
            d[i][0] = d[i-1][0] if obstacleGrid[i][0] == 0 else 0
        for j in range(1,n):
            d[0][j] = d[0][j-1] if obstacleGrid[0][j] == 0 else 0
        for i in range(1,m):
            for j in range(1,n):
                print(i,j)
                d[i][j] = d[i][j-1] + d[i-1][j] if obstacleGrid[i][j] == 0 else 0

        return d[m-1][n-1]

    '''java
    // Time: O(m*n), Space: O(n)
    public int uniquePathsWithObstaclesOn(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[] d = new int[n];
        d[0] = grid[0][0] == 1 ? 0 : 1;

        for (int i = 0; i < m; ++i) {
        d[0] = grid[i][0] == 1 ? 0 : d[0];
        for (int j = 1; j < n; ++j) {
            d[j] = grid[i][j] == 1 ? 0 : d[j] + d[j-1];
        }
        }
        return d[n-1];
    }
'''

if __name__ == "__main__":
    s =Solution()
    print(s.uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))

