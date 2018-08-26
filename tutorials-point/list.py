#!/usr/bin/python3

num_list = list(range(5))

str_list = ["a", "b", "c"]
print()
print("str_list: ", str_list ) 

hetero_list = ["a", 10, list(range(5))]
print()
print("hetero_list: ", hetero_list ) 

print()
print("num_list: ", num_list ) 
print("accessing value")
print("list[2]: ", num_list[2])

print("delete item 3: del list[2]")
del num_list[2]
print("num_list", num_list)

print()
print()
print("basic operation")
num_list = list(range(5))
print("len(num_list): ", len(num_list))
print("num_list + num_list: ", num_list + num_list)
print("num_list * 4: ", num_list * 4)
print("3 in num_list: ", 3 in num_list)

print()
print("iteration: for item in num_list: print('item') ")
for item in num_list: print("item: ", item)

print()
print("slicing")
print("num_list[:]", num_list[:])
print("num_list[1:2]", num_list[1:2])
print("num_list[:-1]", num_list[:-1])

print()
print("built-in function")
print(num_list, " len(num_list)", len(num_list))
print(num_list, " max(num_list)", max(num_list))
print(str_list, " max(str_list)", max(str_list))
print(tuple(range(5)), " list(tuple(range(5))): ", list(tuple(range(5))))
print("list('String'): ", list("String"))


print()
print("list function")
print("list:", num_list)

num_list.extend(range(11,15))
print("list.extend(range(11,15)): ", num_list)

num_list.append(1)
print("list.append(1): ", num_list)
print(num_list, ".count(1): ", num_list.count(1))

print(num_list, ".index(1): ", num_list.index(1))

num_list.insert(5, 100)
print("list.insert(5, 100): ", num_list)
