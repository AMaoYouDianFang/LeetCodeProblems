class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        value = [1000, 500, 100, 50, 10, 5, 1]
        res = ''
        for i  in range(0,7,2): #0,2,4,6 位 对应的1000，100，10，1
            x = num // value[i]
            if x < 4:
                for j in range(1, x+1):   #有几个1000， 对应出现几个M  注意边界
                    res = res + roman[i]
            elif x == 4:
                res = res + roman[i] + roman[i - 1]  #CD是400
            elif x > 4 and x < 9:
                res += roman[i-1]
                for j in range(6,x+1):
                    res = res + roman[i]
            elif x ==9:
                res = res + roman[i] + roman[i-2]
            num = num % value[i]
        return res