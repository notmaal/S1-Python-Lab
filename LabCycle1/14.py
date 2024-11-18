# sort dictionary
dictionary = {"pineapple" : 23, "apple" : 2, "banana" : 32}
print(f"The dictionary in sorted order is: {dict(sorted(dictionary.items()))}")
print(f"The dictionary in sorted descending order is: {dict(sorted(dictionary.items(), reverse=True))}")