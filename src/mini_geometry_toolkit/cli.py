from .circle import area as circle_area, circumference
from .square import area as square_area, perimeter as square_perimeter
from .rectangle import area as rect_area, perimeter as rect_perimeter
from .visualizer import plot_circle, plot_square, plot_rectangle

def run():
    print("=== Mini Geometry Toolkit ===")

    print("Choose a shape:")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")

    choice = input("Enter choice (1/2/3): ")

    # 🔵 CIRCLE
    if choice == "1":
        r = float(input("Enter radius: "))
        print("Area:", circle_area(r))
        print("Circumference:", circumference(r))

        show = input("Show graph? (y/n): ")
        if show.lower() == "y":
            plot_circle(r)

    # 🟩 SQUARE
    elif choice == "2":
        s = float(input("Enter side length: "))
        print("Area:", square_area(s))
        print("Perimeter:", square_perimeter(s))

        show = input("Show shape? (y/n): ")
        if show.lower() == "y":
            plot_square(s)

    # ▭ RECTANGLE
    elif choice == "3":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print("Area:", rect_area(l, w))
        print("Perimeter:", rect_perimeter(l, w))

        show = input("Show shape? (y/n): ")
        if show.lower() == "y":
            plot_rectangle(l, w)

    else:
        print("Invalid choice")