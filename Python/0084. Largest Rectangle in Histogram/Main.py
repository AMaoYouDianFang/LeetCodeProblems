class Solution:
    #队列
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
    
    def largestRectangleArea1(self, heights):
        maxArea = 0
        for i in range(len(heights)):
            r, l = i, i
            #计算以heights[i]为高度
            while( l >= 0 and heights[i] <= heights[l] ):
                l -= 1
            while (r < len(heights) and heights[i] <= heights[r]):
                r += 1
            maxArea = max(maxArea, heights[i] * (r-l-1))
        return maxArea
            




if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea([2,1,5,6,2,3]))
    print(s.largestRectangleArea1([2,1,5,6,2,3]))

#思路：

#在heights数组后加上一个高度为0的哨兵，以正确计算最后一个柱子；
#栈中存放一组高度值比当前元素高的柱子的下标；
#遍历数组：
#若当前柱子比栈顶（当前阶段最高的柱子）的高度低，说明当前元素无法和栈中保存的柱子们构成一个面积较大的矩形（强行加载一起的话当前柱子就成了木桶效应中的短板，面积反而会减小）。此时将栈中比当前柱子高的都弹出并计算面积，更新最大面积。
#否则说明此柱子并非短板，加上它可能增加当前正在构建的矩形的面积，直接将其下标压栈。