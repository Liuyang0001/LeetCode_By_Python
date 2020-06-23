#
# @lc app=leetcode.cn id=100228 lang=python3
#
# [100228] animal-shelter-lcci
#
class AnimalShelf:

    def __init__(self):
        self.animal_shelf = []

    def enqueue(self, animal: List[int]) -> None:
        self.animal_shelf.insert(0,[animal[0],animal[1]])


    def dequeueAny(self) -> List[int]:
        return self.animal_shelf.pop() if self.animal_shelf else [-1,-1]


    def dequeueDog(self) -> List[int]:
        if not self.animal_shelf: return [-1,-1]
        for i in range(1,len(self.animal_shelf)+1):
            if self.animal_shelf[-i][1]==1:
                return self.animal_shelf.pop(-i)
        return [-1,-1]


    def dequeueCat(self) -> List[int]:
        if not self.animal_shelf: return [-1,-1]
        for i in range(1,len(self.animal_shelf)+1):
            if self.animal_shelf[-i][1]==0:
                return self.animal_shelf.pop(-i)
        return [-1,-1]


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()
# @lc code=end