'''
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

来源：力扣（LeetCode）
链接：hteps://leetcode-cn.com/problems/rotate-image
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:

#         n = len(matrix[0])
#         # 转置矩阵
#         for i in range(n):
#             for j in range(i, n):
#                 matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

#         # 翻转每行
#         for i in range(n):
#             matrix[i].reverse()


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anext_ything, modify matrix in-place instead.
        """
        # 求转90度后下一个坐标的位置
        def next_xy(x, y, s):
            return y, s - 1 - x
            
        n = len(matrix)
        # 行数
        for i in range(n):
            l = n - i * 2
            if l < 2:
                break
            # 列数
            for j in range(l-1):
                x, y = 0, j
                tem = matrix[x + i][y + i]
                # 四条边上各有一个点
                for _ in range(4):
                    next_x, next_y = next_xy(x, y, l)
                    # print(x, y, next_x, next_y)
                    # print(t, matrix[next_x+i][next_y+i])
                    tem_new = matrix[next_x+i][next_y+i]
                    matrix[next_x+i][next_y+i] = tem
                    x, y, tem = next_x, next_y, tem_new


if __name__ == "__main__":
    S = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(matrix)
    S.rotate(matrix)
    print(matrix)
