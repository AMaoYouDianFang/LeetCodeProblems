class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0: return 'Zero'
        res = self.convent(num % 1000)
        v = ["Thousand", "Million", "Billion"]
        for i in range(3):
            num = num //1000
            if (num % 1000 != 0):
                res = self.convent(num % 1000) + ' ' +v[i] + ' ' + res
        while res[-1] == ' ':
            res = res[:-1]

        return res
    def convent(self, num):  #将3位数子转换
        v1 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        v2 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        res = ''
        a = num // 100 #
        b = num % 100 #个位和十位
        c = num % 10
        if b< 20:
            res = v1[b]
        else:
            temp = '' if c == 0 else ' ' + v1[c]
            res = v2[b//10] + temp
        if a > 0:
            temp2 = '' if b ==0 else ' ' + res
            res = v1[a] + ' Hundred' + temp2
        return res


if __name__ == "__main__":
    num = 123456
    s = Solution()
    print(s.numberToWords(num))