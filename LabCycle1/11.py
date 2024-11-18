# swap first and last letter of string

text = input("Enter the string: ")
text = text[-1] + text[1:-1] + text[:1]
print("The string after swapping: ",text)
