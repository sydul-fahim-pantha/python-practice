#!/usr/bin/python3


print()
print("Function can have four types of argument")

print()
print("Required argument: def func1(arg1)")
print("Invocation: func1(\'value\')")

def func1(arg1): 
    print("arg1: ", arg1)
    return
func1("arg")    


print()
print("Keyword argument: def func(id, age, name)")
print("Invocation: func(name ='Bla', id = 10, age = 24)")
print("NOTE: One can change the order of the argument")

def func2(id, age, name): 
    print("id: ", id, " age: ", age, " name: ", name)
    return
func2(name = "Bla", id = 10, age = 24)    


print()
print("Default argument: def func(id = 100)")
print("Invocation: func(10) or func()")
print("NOTE: If no argument specified the default value == 10 is used")

def func3(id = 100): 
    
    if id == 10: print("using default value id: ", id)
    else : print("value passed by argument id: ", id)
    return
func3(555)
func3()    


print()
print("Variable length argument: def func(*vararg)")
print("Invocation: func() or func(10, 20) or func(10,...n)")
print("NOTE: the variable is a tuple ")

def func4(*items): 
    print("inside var-arg func with argument: ", items)
    for item in items: print(item)
    return
func4()
func4(10)
func4(10, 20, 30)    