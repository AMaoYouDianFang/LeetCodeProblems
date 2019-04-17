class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            mid = (l + r) // 2
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                l = mid + 1
            else:
                r = mid - 1
        return l-1  #!!!返回l-1

if __name__ == "__main__":
    s = Solution()
    res = s.mySqrt(8)
    print(res)
