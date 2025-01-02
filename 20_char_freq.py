text = input("Enter the string: ").lower()
c = input("Enter the character: ").lower()
count = 0
for char in text:
    if char == c:
        count += 1
print(f"The frequency of {c} in {text} is {count}")