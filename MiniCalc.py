def add(x,y):
    value = x + y
    return value

def subtract(x,y):
    value = x - y
    return value

def multiply(x,y):
    value = x * y
    return value

def divide(x,y):
    value = x / y
    return value


exitCase = False
while(exitCase == False):
    UserInput = int(input("Select an arithmetic operation: 1)Add \n2)Subtract \n3)Multiply \n4)Divide \n"))
    num1 = 0
    num2 = 0

    if UserInput == 1:
        num1 = int(input("Select the first number of the operation \n"))
        num2 = int(input("Select the second number of the operation \n"))
        result = add(num1,num2)
        print(result)
        exitCase = True
    if UserInput == 2:
        num1 = int(input("Select the first number of the operation \n"))
        num2 = int(input("Select the second number of the operation \n"))
        result = subtract(num1, num2)
        print(result)
        exitCase = True
    if UserInput == 3:
        num1 = int(input("Select the first number of the operation \n"))
        num2 = int(input("Select the second number of the operation \n"))
        result = multiply(num1, num2)
        print(result)
        exitCase = True
    if UserInput == 4:
        num1 = int(input("Select the first number of the operation \n"))
        num2 = int(input("Select the second number of the operation \n"))
        result = divide(num1, num2)
        print(result)
        exitCase = True
    if UserInput != 1 or 2 or 3 or 4:
        print("wrong input please try again")


