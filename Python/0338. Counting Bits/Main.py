from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num+1):
            count = 0 
            while i != 0:
                i &= i-1
                count += 1
            res.append(count)
        return res
    #动态规划
    def countBits1(self, num: int) -> List[int]:
        d = [0] * (num+1) 
        for i in range(1, num+1):
            d[i] = d[i & (i-1)] + 1
        return d


if __name__ == "__main__":
    s = Solution()
    print(s.countBits(2))
    print(s.countBits1(2))
            