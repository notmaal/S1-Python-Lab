text = input("Enter the string: ")
c = input("Enter the character: ")
count = 0
for char in text:
    if char == c:
        count += 1
print(f"The frequency of {c} in {text} is {count}")