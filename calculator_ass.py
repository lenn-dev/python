
operation = True
while operation:
    
    num1 = int(input("Choose a number :"))
    num2 = int(input("Choose another number :"))
    oper = input("Choose an operator\n Options are: +, -, *, or /. \n Write 'exit' to finish\n")
    if oper != "+"or"-"or"*"or"/":
        print("You put wrong operator. Try again.")

    if oper == exit:
        operation = False
    else:
        if oper == "+" :
            print( num1 + num2 )
        elif oper == "-":
            print( num1 - num2 )
        elif oper == "*":
            print( num1 * num2 )
        elif oper == "/":
            print( num1 / num2 )
     
    
   