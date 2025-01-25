class area:
    def __init__(self,lenght,breadth):
        self.lenght = 0.0
        self.breadth = 0.0

    def cal_area(self):
        print(self.lenght*self.breadth)

ar = area(13.33,23.20)
print(ar.lenght)
ar.cal_area()