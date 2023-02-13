import math
type = input()

if type == "square":
    square_side = float(input())
    square_area = math.pow(square_side, 2)
    print(f"{square_area:.3f}")
elif type == "rectangle":
    width = float(input())
    length = float(input())
    rectangle_area = width * length
    print(f"{rectangle_area:.3f}")
elif type == "circle":
    r = float(input())
    circle_area = math.pi * math.pow(r, 2)
    print(f"{circle_area:.3f}")
elif type == "triangle":
    triangle_side = float(input())
    h = float(input())
    triangle_area = triangle_side * h / 2
    print(f"{triangle_area:.3f}")