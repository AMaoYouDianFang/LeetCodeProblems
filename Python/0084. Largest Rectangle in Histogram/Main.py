class Solution:
    def largestRectangleArea(self, heights):
        if not heights :
            return  0
        heights.append(0)
        stack = []
        area, maxArea= 0, 0
        
        for i  in range (len(heights)):
            h = 0 if i == len(heights) else heights[i]
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                start = stack[-1] if stack else -1
                area = heights[height] * (i - start -1)
                maxArea = max(maxArea,area)
            stack.append(i)
        return maxArea

if __name__ == "__main__":
    s = Solution()
    res = s.largestRectangleArea([1])
    print(res)

#思路：

#在heights数组后加上一个高度为0的哨兵，以正确计算最后一个柱子；
#栈中存放一组高度值比当前元素高的柱子的下标；
#遍历数组：
#若当前柱子比栈顶（当前阶段最高的柱子）的高度低，说明当前元素无法和栈中保存的柱子们构成一个面积较大的矩形（强行加载一起的话当前柱子就成了木桶效应中的短板，面积反而会减小）。此时将栈中比当前柱子高的都弹出并计算面积，更新最大面积。
#否则说明此柱子并非短板，加上它可能增加当前正在构建的矩形的面积，直接将其下标压栈。