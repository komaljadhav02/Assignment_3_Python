#  Write a Python function to sum all the numbers in a list.

def sum():
    size= int(input("Enter the size :"))  #to take number of elements in a list
    lst = []
    for i in range(size):
        element=int(input("Enter number:"))  #to take numbers for addition
        lst.append(element)
    print(lst)   # printing original list
    total = 0
    for i in lst:
        total += i
    return total
print(sum())    #calling function