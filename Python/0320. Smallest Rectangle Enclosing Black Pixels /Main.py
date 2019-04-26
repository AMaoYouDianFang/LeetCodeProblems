'''2-18
这道题给我们一个二维矩阵，表示一个图片的数据，其中1代表黑像素，0代表白像素，
现在让我们找出一个最小的矩阵可以包括所有的黑像素，还给了我们一个黑像素的坐标
[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2,
Return 6.
'''

#Brute Force的方法，这种方法的效率不高，遍历了整个数组，如果遇到了1，就更新矩形的返回

class Solution:
    def minArea(image, x, y):
        left, right = x, x
        up, down = y, y 
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == 1:
                    left = min(j, left)
                    right = max(j, right)
                    up = min(i, up)
                    down = max(i,down)
        return (right - left + 1) * (down - up + 1)