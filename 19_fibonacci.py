limit = int(input("Enter the limit: "))
a = 0  # a = b
b = 1  # b = a + b
print(f"The {limit} fibonocci numbers are: ", end="")
for _ in range(limit):
    print(a, end=" ")
    temp = a
    a = b
    b = temp + b