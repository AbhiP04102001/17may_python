import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)

    circle_area = circle.area()
    circle_perimeter = circle.perimeter()

    print(f"Circle Area: {circle_area:.2f}")
    print(f"Circle Perimeter: {circle_perimeter:.2f}")
