#!/usr/bin/python3

s1 = "str1"
s2 = "str2"

print()
print()
print("s1: ", s1)
print("s2: ", s2) 

print("s1[0]: ", s1[0])
print("s1[-1]: ", s1[-1])

print()
print("s1[0:0]: ", s1[0:0])
print("s1[0:1]: ", s1[0:1])
print("s1[:1]: ", s1[:1])

print()
print("s1[0:2]: ", s1[0:2])
print("s1[:2]: ", s1[:2])

print()
print("s1[0:-1]: ", s1[0:-1])
print("s1[0:]: ", s1[0:])
print("s1[:-1]: ", s1[:-1])

print()
print("s1[:]: ", s1[:])
print("s1[0:4]: ", s1[0:4])


print()
print("s1*2: ", s1 * 2)


print()
print("s in s1: ", str('s' in s1))
print("1 in s1: ", str('1' in s1))


print()
print("s in s1: ", str('s' in s1))
print("1 in s1: ", str('1' in s1))



print()
print()
print("Triple quoted string ")
s3 = para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print(s3)



