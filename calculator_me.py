import math

#image

first_num = float(input("Enter the first number: "))

def calc(f_num,oper,s_num):
    """Function for calculating"""
    if oper == '+':
        return f_num + s_num
    elif oper == '-':
        return f_num - s_num
    elif oper == '*':
        return f_num * s_num
    elif oper == '/':
        return f_num / s_num

end = False

while not end:
    operation = input("Pick an operation:\n+\n-\n*\n/\n")
    next_number = float(input("Enter the next number: "))
    res = calc(first_num,operation,next_number)
    print(f"{first_num} {operation} {next_number} = {res}")
    another_cal = input("Type 'y' to continue calculating, or 'n' to start a new calculation: ")
    if another_cal == 'y':
        first_num = res
        end = False
    elif another_cal == 'n':
        end = True
