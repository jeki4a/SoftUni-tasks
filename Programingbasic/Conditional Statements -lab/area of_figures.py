import math

figure = str(input())

if figure == "square":
    side = float(input())
    area = side ** 2
    print(round(area, 3))

elif figure == "rectangle":
    length = float(input())
    width = float(input())
    area = length * width
    print(round(area, 3))

elif figure == "circle":
    radius = float(input())
    area = math.pi * radius ** 2
    print(round(area, 3))

elif figure == "triangle":
    base = float(input())
    height = float(input())
    area = 0.5 * base * height
    print(round(area, 3))

