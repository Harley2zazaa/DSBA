"""Point"""
class Point:
    def __init__(self, x, y, x2, y2):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.value = 0

    def calculate_distance(self) :
        self.value = ((self.x2 - self.x)**2 + (self.y2 - self.y)**2) ** 0.5
    
    def output(self):
        return self.value

ans = Point(float(input()),float(input()),float(input()),float(input()))
ans.calculate_distance() # run method in class
print(f"{ans.output():.2f}")
