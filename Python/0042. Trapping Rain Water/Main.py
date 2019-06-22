class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = len(height)
        leftmax = -1
        rightmax = -1
        d = []
        res = 0
        for i in range(l):
            leftmax = max(leftmax, height[i])
            d.append(leftmax)
        for j in range(l-1, -1, -1):
            rightmax = max(rightmax, height[j])
            res = res + min(rightmax, d[j]) - height[j]
        return res



if __name__ == "__main__":
    s = Solution()
    res = s.trap( [0,1,0,2])  
    print(res)                      


