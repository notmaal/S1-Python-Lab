# print given pyramid
# 1
# 2 4
# 3 6 9
# 4 8 12 16
step = int(input("Enter the step: "))
for i in range(1, step + 1):
    for j in range(1, i+1):
        print(i * j, end=" ")
    print()