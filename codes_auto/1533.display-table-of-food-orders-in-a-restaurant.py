#
# @lc app=leetcode.cn id=1533 lang=python3
#
# [1533] display-table-of-food-orders-in-a-restaurant
#
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        dic = {}
        menue = set()
        for order in orders:
            table = order[1]
            dic.setdefault(table,{})
            for i in order[2:]:
                menue.add(i)
                dic[table][i] = dic[table].get(i,0)+1
        # print(dic)
        menue = sorted(menue)
        table = sorted(dic.keys(),key= lambda x:int(x))
        # dic.sort(key= lambda x:int(x[0]))
        # print(menue,table)
        # print(dic)
        res = [["Table"]+menue]
        for tab in table:
            tem = [tab]
            for i in menue:
                tem.append(str(dic[tab].get(i,0)))
            res.append(tem)
        return res
# @lc code=end