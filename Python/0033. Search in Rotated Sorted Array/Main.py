'''
二分搜索法的关键在于获得了中间数后，判断下面要搜索左半段还是右半段，
我们观察上面红色的数字都是升序的，由此我们可以观察出规律，
如果中间的数小于最右边的数，则右半段是有序的，
若中间数大于最右边数，则左半段是有序的，
我们只要在有序的半段里用首尾两个数组来判断目标值是否在这一区域内，
这样就可以确定保留哪半边了
'''
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
        
