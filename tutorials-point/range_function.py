#!/usr/bin/python3

print()
	
var = range(5)
print("range(5): ", var)

list = list(var)
print("list(range(5)): ", list)


print("\n\niterate the list(range(5)): ", list)
for num in list: print("num: ", num)


print("\n\nprint the index and value: ", list)
for index in range(len(list)): print("index: ", index)




