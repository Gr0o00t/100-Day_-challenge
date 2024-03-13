def calculator():
    import Calculation as c
    operation= {"+":"add", "-":"Subtract", "*":"Multiply", "/":"Divide"}
    num1=float(input("First Number "))
    for symbol in operation:
        print(f"Please press {operation[symbol]} for {symbol}")

    should_continue=True
    while should_continue:
        operation_symbol=input("Please choose from above symbol")
        num2=float(input("Second Number"))
        #calulation_function=operation[operation_symbol]
        print(f"{operation[operation_symbol]}")
        answer=c.calulation_function(operation_symbol,num1,num2)

        print(f"{num1}{operation_symbol}{num2} = {answer}")

        if input("Type Y : to use the previous result, \n N : to enter a new number").upper()== "Y":
            num1=answer
        else:
            should_continue=False
            calculator()

calculator()