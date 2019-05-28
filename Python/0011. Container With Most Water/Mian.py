class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        maxarea = 0
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            maxarea = max(maxarea, area)
            if height[i] < height[j]:
                i +=1
            else:
                j -= 1
        return maxarea
if __name__ == "__main__":
    s =Solution()
    res= s.maxArea([1,8,6,2,5,4,8,3,7])
    print(res)

