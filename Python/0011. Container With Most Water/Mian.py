class Solution:
    def maxArea(self, height):
        l =len(height)
        s = 0
        e = l-1
        maxarea =0
        while s < e:
            if height[s] <= height[e]:
                area = height[s] *(e-s)
                s += 1
            else:
                area = height[e] *(e-s)
                e -= 1
            
            maxarea = max(maxarea, area)
        return maxarea
if __name__ == "__main__":
    s =Solution()
    res= s.maxArea([1,8,6,2,5,4,8,3,7])
    print(res)

