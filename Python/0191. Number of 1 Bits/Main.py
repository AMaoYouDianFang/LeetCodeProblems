class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n != 0:
            n = n & (n-1) #消去n最后一个1
            count += 1
        return count

if __name__ == "__main__":
    s = Solution()
    print(s.hammingWeight(3))
        