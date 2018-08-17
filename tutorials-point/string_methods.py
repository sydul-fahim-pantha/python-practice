#!/usr/bin/python3
import base64

s1 = "str1"

print()
print("s1.capitalize(): ", s1.capitalize())

print()
print("s1.center(10, w): ", s1.center(10, 'w'))

print()
str = "this is string example....wow!!!"
sub = 'i'
print("str: ", str)
print ("str.count('i') : ", str.count(sub))
sub = 'exam'
print ("str.count('exam', 10, 40) : ", str.count(sub,10,40))


def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))

def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')

print()
Str = "this is string example....wow!!!";
Str = stringToBase64(Str);

print("Encoded String: ", Str)
print("Decoded String: ", base64ToString(Str))
