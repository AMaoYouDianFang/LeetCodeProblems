# 1,2,3,4,5,6,7,8,9,10,11
#第10个数是0 这里把10 看成0和1

# 那么这道题的关键就是要找出第N位所在的数字，然后可以把数字转为字符串，这样直接可以访问任何一位。
# 那么我们首先来分析自然数序列和其位数的关系，前九个数都是1位的，然后10到99总共90个数字都是两位的，
# 100到999这900个数都是三位的，可以定义个变量cnt，初始化为9，然后每次循环扩大10倍，再用一个变量len
# 记录当前循环区间数字的位数，另外再需要一个变量start用来记录当前循环区间的第一个数字，我们n每次
# 循环都减去len*cnt (区间总位数)，当n落到某一个确定的区间里了，那么(n-1)/len就是目标数字在该
# 区间里的坐标，加上start就是得到了目标数字，然后我们将目标数字start转为字符串，(n-1)%len
# 就是所要求的目标位，最后别忘了考虑int溢出问题，我们干脆把所有变量都申请为长整型的好了
class Solution:
     def findNthDigit(self, n):
         lng, cnt, start = 1, 9, 1
         while n > lng * cnt:
             n -= lng * cnt
             lng += 1
             cnt *= 10
             start *= 10
         start += (n - 1) / lng
         print(start)
         t = str(start)
         return int(t[(n - 1) % lng]) ;  

if __name__ == "__main__":
    s = Solution()
    res = s.findNthDigit(15)
    print(res)