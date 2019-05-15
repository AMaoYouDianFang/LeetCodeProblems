from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        i = 0
        j = l - 1
        while i< j:
            temp = s[j]
            s[j] = s[i]
            s[i] = temp
            i += 1
            j -= 1

if __name__ == "__main__":
    s = Solution()
    l = ["h","e","l","l","o"]
    s.reverseString(l)
    print(l)
            
  