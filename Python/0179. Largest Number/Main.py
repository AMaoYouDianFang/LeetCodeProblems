from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        num = [str(x) for x in nums]
        key = cmp_to_key(lambda x,y: int(y+x)-int(x+y))
        #关键字函数，接受一个参数，同时返回一个可以用作排序关键字的值
        res = ''.join(sorted(num, key=key)).lstrip('0')
        return res or '0'

#Python lstrip() 方法用于截掉字符串左边的空格或指定字符        
# join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

if __name__ == "__main__":
    s = Solution()
    print(s.largestNumber([10,2]))
