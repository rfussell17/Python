print("Program author: R. Fussell")
print("ID#: 3417846")
print("this program is using python 3")
print("Program 4 - Functions")
print("")

# this program accepts input for shape they wish to measure in area or perimeter, and calculates + prints results


class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y


class Circle:
    def __init__(self, x):
        self.x = x

    def area(self):
        return 3.14 * self.x ** 2

    def perimeter(self):
        return 2 * 3.14 * self.x

    print("CALCULATIONS MENU")

    print("""
    1) AREA (SQUARE)
    2) AREA (RECTANGLE)
    3) AREA (CIRCLE)
    4) PERIMETER (SQUARE)
    5) PERIMETER (RECTANGLE)
    6) PERIMETER (CIRCLE)
    7) EXIT""")


choice_count = 0
choice_limit = 20
while choice_count < choice_limit:

    choice = input("INPUT MENU CHOICE(1,2,3,4,5,6 OR 7)? ")

    if choice == "1":
        print("YOU HAVE CHOSEN AREA (SQUARE)")
        x = input("INPUT WIDTH? ")
        y = input("INPUT LENGTH? ")
        square1 = Square(int(x), int(y))
        print("AREA IS ", square1.area())

    elif choice == "2":
        print("YOU HAVE CHOSEN AREA (RECTANGLE)")
        x = input("INPUT WIDTH? ")
        y = input("INPUT LENGTH? ")
        rectangle1 = Rectangle(int(x), int(y))
        print("AREA IS ", rectangle1.area())

    elif choice == "3":
        print("YOU HAVE CHOSEN AREA (CIRCLE)")
        x = input("INPUT RADIUS? ")
        circle1 = Circle(int(x))
        print("AREA IS ", circle1.area())

    elif choice == "4":
        print("YOU HAVE CHOSEN PERIMETER (SQUARE)")
        x = input("INPUT WIDTH? ")
        y = input("INPUT LENGTH? ")
        square1 = Square(int(x), int(y))
        print("PERIMETER IS ", square1.perimeter())

    elif choice == "5":
        print("YOU HAVE CHOSEN PERIMETER (RECTANGLE)")
        x = input("INPUT WIDTH? ")
        y = input("INPUT LENGTH? ")
        rectangle1 = Rectangle(int(x), int(y))
        print(rectangle1.perimeter())

    elif choice == "6":
        print("YOU HAVE CHOSEN PERIMETER (CIRCLE)")
        x = input("INPUT RADIUS? ")
        circle1 = Circle(int(x))
        print("PERIMETER IS ", circle1.perimeter())

    elif choice == "7":
        exit()

    else:
        print("")
        print("Please choose only 1-7")
        print("")
