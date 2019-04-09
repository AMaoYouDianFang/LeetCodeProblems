class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1: return 
        res = ''
        size = 2 * numRows - 2
        for  i in range(numRows):
            for j in range(i, len(s), size):
                res += s[j]  #每行的首字母
                temp = j + size - 2*i
                if i!=0 and i!= numRows-1 and temp < len(s):
                    res += s[temp]
        return res
        