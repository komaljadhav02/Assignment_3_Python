# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def string_cal():                            #defining function

    str = input("Enter the string: ")        #taking string from user
    count={"UPPER_CASE":0, "LOWER_CASE":0}

    for i in str:
        if i.isupper():
           count["UPPER_CASE"]+=1
        elif i.islower():
           count["LOWER_CASE"]+=1
        else:
            pass
    print ("Original String : ", str)

    print ("No. of Upper case letters : ", count["UPPER_CASE"]) #printing count of uppercase letters

    print ("No. of Lower case letters : ", count["LOWER_CASE"])  #printing count of lowercase letters

string_cal()   #calling function