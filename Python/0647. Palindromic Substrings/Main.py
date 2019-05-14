class Solution:
    #动态规划
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        d = [[False] * l for i in range(l)]
        count = 0
        for i in range(l,-1,-1): #要从后向前
            for j in range (i,l): #两层循环写错了
                print(i,j)
                if i==j: 
                    d[i][j] = True
                elif i+1 == j: 
                    d[i][j] = s[i] == s[j]
                else: 
                    d[i][j] = (s[i]==s[j]) and d[i+1][j-1]
                if d[i][j]:
                    count += 1
        return count
    
    def helper(self, s, left, right):
        count = 0
        while left>=0 and right < len(s) and s[left] == s[right]:
            count+= 1
            left -= 1
            right +=1 
        return count

    def countSubstrings1(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count+= self.helper(s,i,i)
            count += self.helper(s,i,i+1)
        return count




if __name__ == "__main__":
    s = Solution()
    print(s.countSubstrings1('aaa'))