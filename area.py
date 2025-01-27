def calculate_area():
    print("Choose a shape to calculate the area:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Circle")
    print("5. Sector")
    print("6. Ellipse")
    print("7. Trapezium")
    print("8. Parallelogram")
    print("9. Rhombus")
    print("10. Kite")
    print("11. Pentagon")
    print("12. Hexagon")
    print("13. Octagon")
    print("14. Annulus")
    print("15. Quadrilateral")
    print("16. Regular Polygon")
    print("17. Exit")

    choice = input("Enter your choice (1-17): ")

    if choice == "1":
        # Square
        side = float(input("Enter the side length of the square: "))
        area = side**2
        print(f"The area of the square is: {area}")

    elif choice == "2":
        # Rectangle
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print(f"The area of the rectangle is: {area}")

    elif choice == "3":
        # Triangle
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is: {area}")

    elif choice == "4":
        # Circle
        radius = float(input("Enter the radius of the circle: "))
        area = 3.14159 * radius ** 2
        print(f"The area of the circle is: {area}")

    elif choice == "5":
        # Sector
        radius = float(input("Enter the radius of the sector: "))
        angle = float(input("Enter the angle of the sector in degrees: "))
        area = (angle / 360) * 3.14159 * radius ** 2
        print(f"The area of the sector is: {area}")

    elif choice == "6":
        # Ellipse
        major_axis = float(input("Enter the length of the major axis: "))
        minor_axis = float(input("Enter the length of the minor axis: "))
        area = 3.14159 * (major_axis / 2) * (minor_axis / 2)
        print(f"The area of the ellipse is: {area}")

    elif choice == "7":
        # Trapezium
        base1 = float(input("Enter the first base of the trapezium: "))
        base2 = float(input("Enter the second base of the trapezium: "))
        height = float(input("Enter the height of the trapezium: "))
        area = 0.5 * (base1 + base2) * height
        print(f"The area of the trapezium is: {area}")

    elif choice == "8":
        # Parallelogram
        base = float(input("Enter the base of the parallelogram: "))
        height = float(input("Enter the height of the parallelogram: "))
        area = base * height
        print(f"The area of the parallelogram is: {area}")

    elif choice == "9":
        # Rhombus
        diagonal1 = float(input("Enter the first diagonal of the rhombus: "))
        diagonal2 = float(input("Enter the second diagonal of the rhombus: "))
        area = 0.5 * diagonal1 * diagonal2
        print(f"The area of the rhombus is: {area}")

    elif choice == "10":
        # Kite
        diagonal1 = float(input("Enter the first diagonal of the kite: "))
        diagonal2 = float(input("Enter the second diagonal of the kite: "))
        area = 0.5 * diagonal1 * diagonal2
        print(f"The area of the kite is: {area}")

    elif choice == "11":
        # Pentagon
        side = float(input("Enter the side length of the pentagon: "))
        area = (5 / 4) * (side ** 2) / (3.14159 / 5)
        print(f"The area of the pentagon is approximately: {area}")

    elif choice == "12":
        # Hexagon
        side = float(input("Enter the side length of the hexagon: "))
        area = (3 * 3 ** 0.5 / 2) * (side ** 2)
        print(f"The area of the hexagon is: {area}")

    elif choice == "13":
        # Octagon
        side = float(input("Enter the side length of the octagon: "))
        area = 2 * (1 + 2 ** 0.5) * side ** 2
        print(f"The area of the octagon is: {area}")

    elif choice == "14":
        # Annulus
        outer_radius = float(input("Enter the outer radius of the annulus: "))
        inner_radius = float(input("Enter the inner radius of the annulus: "))
        area = 3.14159 * (outer_radius ** 2 - inner_radius ** 2)
        print(f"The area of the annulus is: {area}")

    elif choice == "15":
        # Quadrilateral (requires all 4 vertices)
        print("This shape requires coordinates of the vertices. Simplified version unavailable.")

    elif choice == "16":
        # Regular Polygon
        num_sides = int(input("Enter the number of sides: "))
        side_length = float(input("Enter the side length: "))
        import math
        area = (num_sides * (side_length ** 2)) / (4 * math.tan(math.pi / num_sides))
        print(f"The area of the regular polygon is: {area}")

    elif choice == "17":
        print("Exiting the program. Goodbye!")
        return

    else:
        print("Invalid choice. Please try again.")

    # Allow the user to calculate again
    print()
    calculate_area()

# Run the program
calculate_area()
