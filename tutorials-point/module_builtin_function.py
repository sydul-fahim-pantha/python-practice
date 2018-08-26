#!/usr/lib/python3

import math
import function_basic
from importlib import reload

print()
print()
print(">>>>>>> dir(math): \n", dir(math))

global_var1 = 10
global_var2 = 100

print()
print()
def func1() :
    func1_local_var1 = 20
    func1_local_var2 = 2000
    print("inside func1")
    print(">>>>>>>>>> locals(): \n", locals())
    print(">>>>>>>>>> globals(): \n", globals())
    
    return

func1()

print()
print()
print("importing the same module for several times using ")
print("importlib.reload(\"function_basic\")")
reload(function_basic)
reload(function_basic)

