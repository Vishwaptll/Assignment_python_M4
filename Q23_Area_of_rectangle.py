#23.Write a Python class named Rectangle constructed by a length and
#    width and a method which will compute the area of a rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

rectangle1 = Rectangle(2,20)

area = rectangle1.compute_area()
print(f"The area of the rectangle is: {area} square units")


