# program to swap 2 numbers

num1, num2 = input("Enter the two numbers: ").split()
print(f"The numbers before swapping: num1 = {num1} and num2 = {num2}")
temp = num1
num1 = num2
num2 = temp
print(f"The numbers after swapping: num1 = {num1} and num2 = {num2}")