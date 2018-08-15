#!/usr/bin/python3

print("\n\nInput your number to check prime")

input = int(input())
actual_input = input
if input < 0: input *= -1
print(actual_input, " ::: ", input)

if input == 0 or input == 1: print(actual_input, " is not a prime")
else: 
  prime = True
  for num in range( 2, input // 2 + 1): 
    print(actual_input, "/", num )
    if input % num == 0:
      print(actual_input, " not a prime")
      break
  else: 
    if prime: print(actual_input, " is a prime")

