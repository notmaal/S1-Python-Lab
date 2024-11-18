a = input("Enter the string: ")           # cooking        len(a)  = 7
if a[len(a) - 3:] == 'ing':               #   a[ 7-3 = 4 : 'to the end']
    a += 'ly'                             # cookingny
else:
    a += 'ing'
print(a)