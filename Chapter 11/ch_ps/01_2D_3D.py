class TwoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector value is {self.i}i + {self.j}j")

class ThreeDvector(TwoDvector):
    def __init__(self,i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector value is {self.i}i + {self.j}j + {self.k}k")

a = TwoDvector(3, 5)
a.show()

b = ThreeDvector(6, 4, 3)
b.show()