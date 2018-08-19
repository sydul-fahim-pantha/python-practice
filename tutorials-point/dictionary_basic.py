#!/usr/bin/python3

print()
print()
print("Dictionry key should be immutable type.")
print("I.e. only number, string and tuple can be a dictionary key")
d1 = {"k1": "v1", "k2": 2, "k3": list(range(5))}
print(d1)

print()
print("Ordering can be achieved using number as key")
d2 = {1: 1, 2: 2, 3: 3}
print(d2)

print()
print("For string key there is no order")
d3 = {"1" : 1, "2" : 2, "3" : 3}
print(d3)


print()
print("Simply iterate using for loop")
d4 = {"k1": "v1", "k2": "v2"}
print("for item in ", d4, " : print()")
for item in {"k1": "v1", "k2": "v2"} : print(item, " : ", d4[item])


