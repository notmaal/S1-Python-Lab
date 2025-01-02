class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth
    
    def area(self):
        return self.__length * self.__breadth
    
    def perimeter(self):
        return 2 * (self.__length + self.__breadth)
    
    def __lt__(self, rect2):
        if self.area() < rect2.area():
            return True
        else:
            return False

    

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
    
    print(rectangle1<rectangle2)