class Solution:
    def isChar(seld, c):
        if ord(c) >= ord('a') and ord(c) <= ord('z') or ord(c) >= ord('0') and ord(c) <= ord('9'):
            return True
        else:
            return False
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i <j:
            while i <j and self.isChar(s[i]) == False: i+=1
            while i <j and self.isChar(s[j]) == False: j-=1
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome('1a2'))