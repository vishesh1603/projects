class myclass:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return(f"({self.x +other.x},{self.y + other.y})")
    
    
n1 = myclass(2,4)
n2 = myclass(3,6)

print(n1+n2)

        