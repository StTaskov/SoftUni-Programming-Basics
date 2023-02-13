from math import pow
from math import pi
type = input()

if type == "square":
    square_size = float(input())
    S_square = pow(square_size, 2)
    print(f'{S_square:.3f}')

elif type == "rectangle":
    width = float(input())
    length = float(input())
    S_rectangle = width * length
    print(f"{S_rectangle:.3f}")

elif type == "circle":
    r = float(input())
    S_circle = pi * pow(r, 2)
    print(f"{S_circle:0.3f}")

elif type == "triangle":
    triangle_side = float(input())
    h = float(input())
    S_triangle = triangle_side * h / 2
    print(f"{S_triangle:.3f}")
