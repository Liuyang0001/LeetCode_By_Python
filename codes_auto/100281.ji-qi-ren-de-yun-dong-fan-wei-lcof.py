#
# @lc app=leetcode.cn id=100281 lang=python3
#
# [100281] ji-qi-ren-de-yun-dong-fan-wei-lcof
#
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def sum_of_bits(a,b):
            res = 0
            for i in str(a)+str(b):
                res+=int(i)
            return res
        que,visited = [(0,0)],[(0,0)]
        while que:
            # que 左侧插入，右侧取值，模拟先进先出
            tem_x,tem_y = que.pop()
            for x_offset,y_offset in [(-1,0),(0,-1),(0,1),(1,0)]:
                x,y = tem_x+x_offset,tem_y+y_offset
                # print("当前：",(x,y))
                if 0<=x<m and 0<=y<n and sum_of_bits(x,y)<=k and (x,y) not in visited:
                    que.insert(0,(x,y))
                    visited.append((x,y))
        # print(visited)
        return len(visited)
# @lc code=end