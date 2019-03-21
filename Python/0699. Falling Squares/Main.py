class Solution:
    def fallingSquares(self, positions) :
        l = len(positions)
       
        height = [0] * l
        for i in range(l):
            longth = positions[i][1]
            left = positions[i][0]
            right = left + longth
            height[i] += longth
            for j in range(i+1, l):
                le = positions[j][0]
                ri = positions[j][1] + le
                if le < right and ri > left:
                    height[j] = max(height[i],height[j])
        res = []
        cur = 0
        for h in height:
            cur = max(cur, h)
            res.append(cur)
        return res


        
        

if __name__ == "__main__":
    s = Solution()
    s.fallingSquares([1,2,3,4,5,6])

        