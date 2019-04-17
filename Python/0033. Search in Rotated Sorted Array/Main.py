#参考的
# 时间复杂度O(log n)

# 思路：

# 1. 先将数组二分，判断target与nums[mid]的关系，若target == nums[mid]，直接返回下标，否则进入第二步；
# 若nums[left] <= nums[mid]，则左子序列是排好序的。
# 2. 同时若target > nums[left] and target < nums[mid]，则且target在其中，对左子序列二分查找即可；否则从第一步开始递归处理右侧旋转数组。
# 3. 若nums[mid] <= nums[right]，则右子序列是排好序的。同时若target > nums[mid] and target < nums[right]，
# 则target在其中，对右子序列二分查找即可；否则从第一步开始递归处理左侧旋转数组。
class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]:  #!!!等于号
                # !!! target >= nums[l] 为了保证能查找到
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target >nums[mid] and target <=nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

if __name__ == "__main__":
    s= Solution()
    res = s.search([4,5,6,7,0,1,2],0)
    print(res)
        
