class Solution(object):
    def trap1(self, height): #指针扫描
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

    def trap(self, height):
        stack = []
        i = 0
        res = 0
        n = len(height)
        while i< n:
            if  stack == [] or height[i] <= stack[-1]:
                stack.append(i)
                i += 1
                
            else:
                t = stack.pop()
                
                if stack == []:
                    continue
                res += (min(height[i], height[stack[-1]]) - height[t]) * (i - stack[-1] -1) 
                print(res)
                
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.trap( [0,1,0,2])  
    print(res)                      


