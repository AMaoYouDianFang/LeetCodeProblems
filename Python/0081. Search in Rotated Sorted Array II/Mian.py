'''
2-11
这道是之前那道 Search in Rotated Sorted Array 
在旋转有序数组中搜索 的延伸，现在数组中允许出现重复数字，
这个也会影响我们选择哪半边继续搜索，
由于之前那道题不存在相同值，我们在比较中间值和最右值时就完全符合之前所说的规律：
如果中间的数小于最右边的数，则右半段是有序的，
若中间数大于最右边数，则左半段是有序的。
而如果可以有重复值，就会出现来面两种情况，
[3 1 1] 和 [1 1 3 1]，对于这两种情况中间值等于最右值时，
目标值3既可以在左边又可以在右边，那怎么办么，对于这种情况其实处理非常简单，
只要把最右值向左一位即可继续循环，如果还相同则继续移，直到移到不同值为止，
然后其他部分还采用 Search in Rotated Sorted Array 在旋转有序数组中搜索 中的方法
'''


class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target: return True
            elif nums[mid] < nums[r]:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[r]:
                if nums[mid] > target and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:   #多了一步
                r = r - 1
        return False

if __name__ == "__main__":
    s = Solution()
    res = s.search([3,1],1)
    print(res)
