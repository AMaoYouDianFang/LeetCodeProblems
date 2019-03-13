class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if not str:
            return False
        strLst = preorder.split(',')
        count = 0
        for i in range(len(strLst)-1):
            if strLst[i] == '#':
                if count > 0:
                    count -= 1
                else:
                    return False
            else:
                count += 1
        if count == 0 and strLst[-1] == '#':
            return True
        else:
            return False


if __name__ == "__main__":
    s =Solution()
    res = s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
    print(res)