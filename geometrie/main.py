from class_triangle import triangle
from class_rectangle import rectangle
from class_circle import circleclass


rectangle_1 = rectangle(1, 1, 4, 4, 1, 1)
circle_1 = circleclass(1, 1, 4, 4, 1 , 1)
triangle_1 = triangle(1, 1, 3, 3, 5, 1)




print(rectangle_1.calc_area())
print(rectangle_1.calc_circumference())

print(circle_1.calc_area())
print(circle_1.calc_circumference())

print(triangle_1.calc_area())
print(triangle_1.calc_circumference())