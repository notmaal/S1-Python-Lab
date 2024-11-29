class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth
    
    def area(self):
        return self.__length * self.__breadth
    
    def perimeter(self):
        return 2 * (self.__length + self.__breadth)
    

# __name__: A special variable that indicates the name of the module.

# If the file is run directly, __name__ is "__main__".
# If the file is imported, __name__ is the module's name.
    
if __name__ == "__main__":        

    length, breadth = input("Enter the length and breadth of first rectangle: ").split(" ")
    rectangle1 = Rectangle(int(length), int(breadth))

    length, breadth = input("Enter the length and breadth of second rectangle: ").split(" ")
    rectangle2 = Rectangle(int(length), int(breadth))

    print(f"The area of first rectangle is: {rectangle1.area()}\n")
    print(f"The area of second rectangle is: {rectangle2.area()}\n")

    print(f"The perimeter of first rectangle is: {rectangle1.perimeter()}\n")
    print(f"The perimeter of second rectangle is: {rectangle2.perimeter()}\n")
    
    if(rectangle1.area() < rectangle2.area()):
        print("The first rectangle has more area than the second")
    elif(rectangle1.area() > rectangle2.area()):
        print("The second rectangle has more area than the first")
    else:
        print("Both the rectangles have same area")