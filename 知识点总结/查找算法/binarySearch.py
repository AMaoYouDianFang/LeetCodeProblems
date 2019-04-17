def binarysearch(nums,target):
    l , r = 0, len(nums)-1
    while (l <= r):
        mid = l + (r - l) // 2  
        if nums[mid] == target:
            return mid 
        elif nums[mid] <= target:
            l = mid + 1
        else:
            r = mid -1
    # return -1 如果没有找到，返回-1
    return l # 返回low表示target若在数组对应的位置，但是实际不在数组中

'''
Low 从 0 起始。只在中位数遇到确定小于目标数时才前进，
并且永不后退。low 一直在朝着第一个目标数的位置在逼近。知道最终到达。

注意点1: mid = l + (r - l) // 2
        写成 mid = （l + r) // 2 在c或java中会溢出
                = (2 * l - l + r) // 2
                = l + (r - l) // 2
'''

if __name__ == "__main__":
    nums = [1,5,3,6,7,2]
    target = 10
    res = binarysearch(nums,target)
    print(res)