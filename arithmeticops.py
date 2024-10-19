# program for arithmetic operations 

def calculate(choice):
    match choice:
        case "1":
            return num1 + num2
        case "2":
            return num1 - num2
        case "3":
            return num1 * num2
        case "4":
            return num1 / num2
        case _:
            return "Error"

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

choice = input("What arithmetic operation would u like to perform? \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \nChoice: ")
answer = calculate(choice)

if answer == "Error":
    print("Wrong choice")
else:
    print(f"The answer is {answer}")
