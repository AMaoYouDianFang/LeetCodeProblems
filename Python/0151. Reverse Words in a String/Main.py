class Solution:
    def reverse(self, s, start, p):
        while start < p:
            temp = s[p]
            s[p] = s[start]
            s[start] = temp
            start += 1
            p -= 1

    def reverseWords(self, s: str) -> str:
        p = 0
        q = 0
        s = list(s) #error
        l = len(s) -1
        while l >= 0 and s[l] == ' ': #error
            l -=1 
        while q <= l:
            start = p
            
            while q<=l and s[q] == ' ':
                q += 1
            while q <= l and s[q] != ' ':
                s[p] = s[q]
                p+= 1
                q+= 1
            self.reverse(s, start, p-1)
            if q <= l:
                s[p] = ' '
                p += 1
        self.reverse(s, 0, p-1) #ERROR
        return "".join(s[0:p]) #ERROR

if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords(
"   hello world! "))
             
            

