from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res = res ^ i ^ nums[i]
        return res
    #思路：假设0～n数字没有缺失的话，对0～n进行异或，可以得到一个确定的数字，
    # 然后对缺失数字的数组进行异或，可以得到另一个数字，这两个数字的异或，就是缺失的数字。
    # 这里的res初始化为n是为i异或 到n，for循环只到n-1 


if __name__ == "__main__":
    s = Solution()
    res = s.missingNumber([0,2,3])
    print(res)