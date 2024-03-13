def calulation_function(opertaion,num1,num2):
    operations= {"+":"add", "-":"Subtract", "*":"Multiply", "/":"Divide"}
    opertaion_1 = (operations[opertaion])
    return opertaion_1(num1,num2)
def add(Num1, Num2):
    return Num1+Num2

def subtract(Num1, Num2):
    return Num1-Num2

def divide(num1,num2):
    return num1/num2

def mulitply(num1,num2):
    return num1*num2

