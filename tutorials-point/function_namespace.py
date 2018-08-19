#!/usr/bin/python3

print()
total = 0   # This is global variable.

def sum( arg1, arg2 ):
   
   total = arg1 + arg2  # Here total is local variable.
   print ("Inside the function local-namespace total : ", total)
   return total

print("Before the function invocation global-namespace total: ", total)

sum( 10, 20 )

print ("After the function invocation global-namespace total : ", total )