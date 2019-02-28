class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1
        res = 0
        maxLeft = maxRight = 0
        while left <=  right:
            if height[left] < height[right]:
                maxLeft = max(maxLeft, height[left])
                res += maxLeft -height[left]
                left += 1
            else:
                maxRight = max(height[right], maxRight)
                res +=  maxRight - height[right] 
                right -=1
        return res               

if __name__ == "__main__":
    s = Solution()
    res = s.trap( [0,1,0,2,1,0,1,3,2,1,2,1])  
    print(res)                      


