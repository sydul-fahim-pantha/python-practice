#!/usr/bin/python3


print()
print()

global_var = -1

print("Before function1 global var: ", global_var)
def change_local_var() : 
    global_var = 1111
    print("Inside function1 global var: ", global_var)

    return

change_local_var()
print("After function1 global var: ", global_var)


print()
print("Before function2 global var: ", global_var)
def change_global_var() :
    global global_var
    global_var = 2222
    print("Inside function2 global var: ", global_var)

    return

change_global_var()
print("After function2 global var: ", global_var)



