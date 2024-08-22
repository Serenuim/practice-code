# outputting message to the console
print("=========== Input data============\n")
print("=========== Select from the options ============= \n")

# options

print("1. Fahrenheit\n")
print("2. Celsuis\n")

# prompting the user to choose from the options
num = int(input("Enter desired number: "))

# checking the user's choice and performing the corresponding conversion
if num == 1:
    Far= int(input("Put ur Celsuis Number Data: "))
    cal= Far *(9/5)+32
    print(cal)


elif num == 2:

    Far =float(input("Enter ur Fahenreit desied number: "))
    cal =(Far -32)*(5/9)
    print(int(cal))
         
