def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calculator():
    num1 = float(input("Enter the first number:  "))

    should_continue = True
    while should_continue:
        for i in operations:
            print(i)
        operation_symbol = input("Pick the operation you want to use from above:  ")

        num2 = float(input("Enter the next number:  "))
        calculation = operations[operation_symbol]
        answer = calculation(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        calc_end = input(f"Do you want to continue calculating with {answer} ?'y'-continue or 'n'-new or 'e'-exit:  ")
        if calc_end == 'y':
            num1 = answer
        elif calc_end == 'n':
            should_continue = False
            calculator()
        elif calc_end == 'e':
            should_continue = False
            print("Thank you for using my calculating app!\nKing regards\nMurodillo")
calculator()