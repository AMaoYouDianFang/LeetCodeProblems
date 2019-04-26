class Solution(object):
    def guessNumber(self, n):
        s = 1  #从1-n 相当于0-n-1 对应加1
        e = n
        while s<=e:
            mid = (s + e) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                e = mid -1
            else:
                s = mid + 1
       