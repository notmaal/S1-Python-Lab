list1 = [x for x in range(1,11)]
print(f"The first list is: {list1}")
list2 = [list1[n] for n in range(0, len(list1)) if list1[n] % 2 != 0]
print(f"The new list is: {list2}")
