text = input("Enter the string: ")
text = text[-1] + text[1:-1] + text[:1]
print(text)