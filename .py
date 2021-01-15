# 
# 
class Class:
    def __init__(self):
        self.L = ["0"]
    
    def SEAT_CREATE(self):
        self.L[0] = "1"
        return self.L
    
    def b(self):
        self.L[0] = "2"
        return self.L

s = Class()

seatData = s.SEAT_CREATE()
lst2 = s.b()

print(seatData)
print(lst2)