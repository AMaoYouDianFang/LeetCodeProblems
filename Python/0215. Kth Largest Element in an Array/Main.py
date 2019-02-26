#https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/167837/Python-or-tm
class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        
        return nums[len(nums) - k]    

if __name__ == "__main__":
    s= Solution()
    nums = [3,2,3,1,2,4,5,5,6]
    print(s.findKthLargest(nums,4))