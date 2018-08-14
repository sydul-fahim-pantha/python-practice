#!/usr/bin/python3

count = 0

print(">>>>>>>>>>>>>>>> simple count loop started >>>>>>>>>>>>")
while count < 9:
   print('The count is:', count)
   count+=1;

print("Good bye!")
print(">>>>>>>>>>>>>>>> simple count loop ended >>>>>>>>>>>>")


print("\n\n>>>>>>>>>>>>>>>> break loop started >>>>>>>>>>>>")
while True :
   print("\nWrite \"exit\" to exit")	
   a = input("Enter anything:")
   print("You entered: ", a)
   if a == "exit": 
      print("Exiting using if") 
      break; 
print(">>>>>>>>>>>>>>>> break loop ended >>>>>>>>>>>>")



print("\n\n>>>>>>>>>>>>>>>> infinite loop started >>>>>>>>>>>>")
a = 10
while a != "exit":
   print("\nWrite \"exit\" to exit")	
   a = input("Enter anything:")
   print("You entered: ", a)
print(">>>>>>>>>>>>>>>> infinite loop ended >>>>>>>>>>>>")





