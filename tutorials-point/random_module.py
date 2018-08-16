#!/usr/bin/python3

import random


print()
print("random.choice(range(5)): ", random.choice(range(5)))

print()
print("random.randrange(10, 15, 1): ", random.randrange(10, 15, 1))
print("random.randrange(15): ", random.randrange(15))


print()
print("random.seed(): ", random.seed())
for n in range(5): print("random.random(): ", random.random())

print()
print("random.seed(100): ", random.seed(100))
for n in range(5): print("random.random(): ", random.random())

print()
print("random.seed(-100): ", random.seed(-100))
for n in range(5): print("random.random(): ", random.random())

list = list(range(5))
print()
print("list(range(5)): ", list)
print()
print("random.shuffle(list(range(5))): ", random.shuffle(list))
print("list(range(5)): ", list)
print()
print("random.shuffle(list(range(5))): ", random.shuffle(list))
print("list(range(5)): ", list)

print()
print("For a given range always returns the same value")
print ("Random Float uniform(5, 10) : ",  random.uniform(5, 10))
print ("Random Float uniform(5, 10) : ",  random.uniform(5, 10))
