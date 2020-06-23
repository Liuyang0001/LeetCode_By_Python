#
# @lc app=leetcode.cn id=100201 lang=python3
#
# [100201] color-fill-lcci
#
class Solution:
    def floodFill(self, image: List[List[int]], \
            sr: int, sc: int, newColor: int) -> List[List[int]]:
        row,col = len(image),len(image[0])
        oldColor = image[sr][sc]        
        def draw(x, y):
            # 要填充的点必须在图像内, 并且与旧的颜色相同, 
            # 并且与新的颜色不同(避免往回填充)
            if 0<=x<row and 0<=y<col and \
                    image[x][y]==oldColor and image[x][y]!=newColor:
                image[x][y] = newColor # 填充当前点
                # 对上下左右四个点递归
                draw(x+1, y)
                draw(x-1, y)
                draw(x, y+1)
                draw(x, y-1)
        draw(sr, sc)
        return image
# @lc code=end