def add(a,b,op):
    result = a+b
    return result
def sub(a,b,op):
    result = a-b
    return result
def multi(a,b,op):
    result = a*b 
    return result
def div(a,b,op):
    result = a/b 
    return result

x = True
while x == True:        
    a = int(input("enter first value: "))
    b = int(input("enter second value: "))
    op = (input("enter operation +,-,*,/"))
    if op == "+":
        addition = add(a,b,op)
        print("addition: ",addition)
    elif op == "-":
        substraction = sub(a,b,op)
        print("substraction: ",substraction)
    elif op == "*":
        multiplication = multi(a,b,op)
        print("multiplication: ",multiplication)
    elif op == "/":
        division = div(a,b,op)
        print("division: ",division)        
    c = input("Enter Y to continue N to exit")
    if c == "N" or c == "n":
        x = False