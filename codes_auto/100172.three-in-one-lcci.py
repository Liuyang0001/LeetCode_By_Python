#
# @lc app=leetcode.cn id=100172 lang=python3
#
# [100172] three-in-one-lcci
#
class TripleInOne:

    def __init__(self, stackSize: int):
        self.stack = []
        # 索引其实无需定义，可根据count计算，但写起来麻烦
        self.stack0_index = 0
        self.stack0_count = 0
        self.stack1_index = 0
        self.stack1_count = 0
        self.stack2_index = 0
        self.stack2_count = 0
        self.maxsize = stackSize


    def push(self, stackNum: int, value: int) -> None:
        # 栈0 push操作
        if stackNum==0 and self.stack0_count<self.maxsize:
            stack_tem = self.stack[self.stack0_index:self.stack0_index+self.stack0_count]
            stack_tem.append(value)
            self.stack0_count+=1
            self.stack = stack_tem + self.stack[self.stack1_index:]
        # 栈1 push操作
        elif stackNum==1 and self.stack1_count<self.maxsize:
            stack_tem = self.stack[self.stack1_index:self.stack1_index+self.stack1_count]
            stack_tem.append(value)
            self.stack1_count+=1
            self.stack = self.stack[:self.stack1_index]+stack_tem+self.stack[self.stack2_index:]
        # 栈2 push操作
        elif stackNum==2 and self.stack2_count<self.maxsize:
            stack_tem = self.stack[self.stack2_index:self.stack2_index+self.stack2_count]
            stack_tem.append(value)
            self.stack2_count+=1
            self.stack=self.stack[:self.stack2_index]+stack_tem
        # 统一修改索引
        self.stack1_index = self.stack0_index + self.stack0_count
        self.stack2_index = self.stack1_index + self.stack1_count

    def pop(self, stackNum: int) -> int:
        res = -1  # 默认返回值
        # 栈0 pop操作
        if stackNum==0 and self.stack0_count>0:
            stack_tem = self.stack[self.stack0_index:self.stack0_index+self.stack0_count]
            res = stack_tem.pop()
            self.stack0_count -= 1
            self.stack = stack_tem + self.stack[self.stack1_index:]
        # 栈1 pop操作
        elif stackNum==1 and self.stack1_count>0:
            stack_tem = self.stack[self.stack1_index:self.stack1_index+self.stack1_count]
            res = stack_tem.pop()
            self.stack1_count -= 1
            self.stack = self.stack[:self.stack1_index]+stack_tem+self.stack[self.stack2_index:]
        # 栈2 pop操作
        elif stackNum==2 and self.stack2_count>0:
            stack_tem = self.stack[self.stack2_index:self.stack2_index+self.stack2_count]
            res = stack_tem.pop()
            self.stack2_count-=1
            self.stack=self.stack[:self.stack2_index]+stack_tem
        # 统一修改索引
        self.stack1_index = self.stack0_index + self.stack0_count
        self.stack2_index = self.stack1_index + self.stack1_count
        return res

    def peek(self, stackNum: int) -> int:
        res = -1  # 默认返回值
        # 栈0 peek操作
        if stackNum==0 and self.stack0_count>0:
            stack_tem = self.stack[self.stack0_index:self.stack0_index+self.stack0_count]
            res = stack_tem[-1]
        # 栈1 peek操作
        elif stackNum==1 and self.stack1_count>0:
            stack_tem = self.stack[self.stack1_index:self.stack1_index+self.stack1_count]
            res = stack_tem[-1]
        # 栈2 peek操作
        elif stackNum==2 and self.stack2_count>0:
            stack_tem = self.stack[self.stack2_index:self.stack2_index+self.stack2_count]
            res = stack_tem[-1]
        return res


    def isEmpty(self, stackNum: int) -> bool:
        if stackNum==0 and self.stack0_count==0:
            res = True
        elif stackNum==1 and self.stack1_count==0:
            res = True
        elif stackNum==2 and self.stack2_count==0:
            res = True
        else: res = False

        return res


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
# @lc code=end