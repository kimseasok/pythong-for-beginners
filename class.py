class Point:
    def move(self):
        print("move")

    def drwa(self):
        print("draw")


point1 = Point()

point1.drwa()

# object attribute

point1.x = 2
point1.y = 10

print(point1.x)


# Contractor

class PointConstractor:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point_contractor = PointConstractor(3, 5)

print(point_contractor.x)

#import module
import module

square_of_four = module.square(4)

print(square_of_four)
