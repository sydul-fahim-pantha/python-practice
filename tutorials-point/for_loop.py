#!/usr/bin/python3

print("\n\n Iterating a the letters of a String")
for letter in 'Python': print('Current Letter :', letter)

print("\n\n Iterating using range function")
for index in range(len('Python')): 
  print('Current index :', index)
  print('Current index character:', "python"[index])

print("\n\n Iterating a list of numbers")
nums = [1, 2, 3]
for num in nums: print('Current number :', num)


print("Good bye!")


