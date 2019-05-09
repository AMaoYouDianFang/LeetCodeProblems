def binarysearch1(nums,target):
    l , r = 0, len(nums)-1
    while l <= r:
        mid = l + (r - l) // 2  
        if nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid -1
    # return -1 如果没有找到，返回-1
    return l # 返回low表示target若在数组对应的位置，但是实际不在数组中

#下面的代码只需要一个return，在求解索达应用可能更方便些，两个方法都是查找第一次出现元素的位置
def binarysearch2(nums, target):
    l , r = 0, len(nums) 
    while l < r:
        mid = (r + l) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l


if __name__ == "__main__":
    nums = [1,3,5,7]
    target = 10
    res1 = binarysearch2(nums,target)
    res2 = binarysearch2(nums,target)
    print(res1, res2)

'''
Low 从 0 起始。只在中位数遇到确定小于目标数时才前进，
并且永不后退。low 一直在朝着第一个目标数的位置在逼近。知道最终到达。

注意点1: mid = l + (r - l) // 2
        写成 mid = （l + r) // 2 在c或java中会溢出
                = (2 * l - l + r) // 2
                = l + (r - l) // 2
'''