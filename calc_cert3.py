# 4. Use Program Library Functions:math.pow() 
import math

# Store calculation history in the list
# 8. Use Array Data Structures
history = []

# Run calculator loop
# 7. Use Loop Structures to Code Logic and Algorithms 
# 6. Use Selection Structures to Code Logic and Algorithms 
# 2. Use Data Types, Operators, and Expressions: Convert input to integer.
# 10. Perform String Manipulation 
while True:
    try:
        # Get user input
        num1_input = input("Enter first number or type 'exit' to quit: ").strip()
        # 6.If the user enters 'exit', the program exits.
        # 4.String library
        if num1_input.lower() == "exit":
            print("Exiting calculator...")
            break
        num1 = int(num1_input)

        num2_input = input("Enter second number or type 'exit' to quit: ").strip()
        if num2_input.lower() == "exit":
            print("Exiting calculator...")
            break
        num2 = int(num2_input)

        oper = input("Choose an operator (+, -, *, /, ** for power) or type 'exit' to quit: ").strip()

        
        if oper.lower() == "exit":
            print("Exiting calculator...")
            break

        # 6.We validate the operator input to ensure it's valid.
        if oper not in ["+", "-", "*", "/", "**"]:
            print("Invalid operator. Please enter +, -, *, /, or ** for power.")
            continue
        
        # Perform calculation
        # 6. Use if-elif to check the operator and decide which operation to perform.
        # 2. Use Data Types, Operators, and Expressions
        if oper == "+":
            result = num1 + num2
        elif oper == "-":
            result = num1 - num2
        elif oper == "*":
            result = num1 * num2
        elif oper == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
        elif oper == "**":
            # 4. Use Program Library Functions: Use math.pow() for power calculation.
            result = math.pow(num1, num2)

        # 2. Use Data Types, Operators, and Expressions: Format the result as a string with two decimal places.
        result_str = f"{num1} {oper} {num2} = {result:.2f}"

        # Fun String Manipulation: Replace certain words to make it playful
        # Print the modified result with '=>'
        fun_result = result_str.replace("=", "=>")
        
        # Slicing: only print result part
        print(f"result is :{result_str[7:]} ")
        print(fun_result)  


        # 8. Use Array Data Structures: Store the result in the 'history' list.
        history.append(result_str)
        print(result_str)

        # 9. Perform File Handling: Open the file in append mode 
        # and Save the formatted result to the file.
        with open("calc_history.txt", "a") as file:
            file.write(result_str + "\n")

    # 6. Use Selection Structures to Code Logic and Algorithms: Handle non-numeric input error.
    except ValueError:
        print("Invalid input. Please enter numeric values.")
