import math
area = str(input())

if area == "square":
    a = float(input())
    print(f'{a*a:.3f}')
elif area == "rectangle":
    a = float(input())
    b = float(input())
    print(f'{a*b:.3f}')
elif area == "circle":
    r = float(input())
    print(f'{math.pi*r*r:.3f}')
elif area == "triangle":
    a = float(input())
    b = float(input())
    print(f'{a*b/2:.3f}')
