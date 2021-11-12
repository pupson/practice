from calc_art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2


# Calculator
def calculator():

    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

    print(logo)

    cont = True
    answer = None

    while cont == True:
        
        if answer == None:
            num1 = float(input("First number: "))
        else:
            num1 = answer
        for key in operations:
            print(f"{key}\n")
        op_symbol = input("Pick an above operation: ")
        num2 = float(input("Second number: "))

        calc_func = operations[op_symbol]
        answer = calc_func(num1, num2)

        print(f"{num1} {op_symbol} {num2} = {answer}" )
        continue_cond = input("Continue calculating (y) / start a new calculation (n) / or exit (x)? ")
        if continue_cond == "n":
            calculator()
        elif continue_cond == "x":
            cont = False

calculator()