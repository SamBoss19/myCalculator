def add (n1 , n2):
    return n1 + n2
def subtract (n1, n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply, 
    "/": divide
}
# function = operations['+']
# function(2,3)
def calculator():
    num1 = float(input("What is the first number "))
    for i in operations:
        print(i)
    choice = True
    while choice == True:
        operator = input("Choose and operartor ")
        num2 = float(input("What is the next number "))
        calculatingFunction = operations[operator]
        answer = calculatingFunction(num1,num2)
        print(f"{num1} {operator} {num2} = {answer}")
        option = input(f"Type 'y' to continue with {answer}, or 'n' to exit ")
        if option == 'y':
            num1 = answer
        else: 
            choice = False
            calculator()

calculator()
