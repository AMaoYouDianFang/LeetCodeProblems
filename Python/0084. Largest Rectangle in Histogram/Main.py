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