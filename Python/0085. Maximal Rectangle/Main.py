from typing import List
class Solution:
    def largestRectangleArea(self, heights):
        if not heights or len(heights) == 0:
            return  0
        heights.append(0)
        stack = []
        area, maxArea= 0, 0
        for r in range(len(heights)):
            while len(stack) > 0 and heights[r] < heights[stack[-1]]:
                h = heights[stack.pop(-1)] #区间之内的高度是递增的，所以取当前的高度
                l = stack[-1] if stack else -1
                maxArea =max(maxArea, (r  -  l - 1)* h)
            stack.append(r)
        return maxArea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix) ==0 or not matrix[0] or len(matrix) ==0:
            return 0
        lst = [0] * len(matrix[0])
        maxArea = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):                lst[j] = lst[j] + 1 if matrix[i][j] == '1' else 0
            area = self.largestRectangleArea(lst)
            maxArea = max(area, maxArea) 
        return maxArea   

if __name__ == "__main__":
    s = Solution()
    print(s.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
  ]))   