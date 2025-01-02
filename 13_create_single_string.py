# add 2 string

def swappos(string1, string2):
    temp = string1[1]       # e     
    string1 = string1[:1] + string2[1:2] + string1[2:]    # h + o + llo
    string2 = string2[:1] + temp + string2[2:]            # w + e + rld
    return string1 + string2       # hollowerld

string1 = input("Enter the first string: ")        # hello
string2 = input("Enter the second string: ")       # world
print(swappos(string1, string2))
