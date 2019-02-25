# 167. Two Sum II - Input array is sorted
class Solution:
    def twoSum(self, nums, target):
        i = 0
        j = len(nums) -1
        
        while(start < end):
            sum = nums[i]+nums[j]  #计算完了会节省时间
            if( sum == target):
                return [i+1,j+1]
            elif(sum > target):
                j -= 1
            elif(sum < target):
                i += 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2,7,11,15],9))