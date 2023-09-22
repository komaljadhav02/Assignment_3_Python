# Write a Python program to reverse a string.

def reverse():
    str = input("Enter the string: ")  #Taking string from user
    rev = str[::-1]                    #reversing the string 
    str = rev                          # storing inside variable str
    return(rev)
print(reverse())                       #calling function

#without function

# str = input("Enter the string: ")
# rev = str[::-1]
# str = rev
# print("Reverse is: ",str)


 

