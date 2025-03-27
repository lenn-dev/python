# Use Library Functions:math.pow() 
import math

# Store calculation history in the list(Array Data structure)
history = []

# Run calculator loop
while True:
    try:
        # Get user input : first number
        num1_input = input("Enter first number or type 'exit' to quit: ").strip()
        # If the user enters 'exit', the program stops.(Selection sturucture)
        if num1_input.lower() == "exit":
            print("Exiting calculator...")
            break
        # converting user input to an integer and store in num1
        num1 = int(num1_input)

        # Get user input : Second number
        num2_input = input("Enter second number or type 'exit' to quit: ").strip()
        # If the user enters 'exit', the program stops.
        if num2_input.lower() == "exit":
            print("Exiting calculator...")
            break
        # converting user input to an integer and store in num2
        num2 = int(num2_input)

        # Get user input : operator
        oper = input("Choose an operator (+, -, *, /, ** for power) or type 'exit' to quit: ").strip()
        # If the user enters 'exit', the program stops.
        if oper.lower() == "exit":
            print("Exiting calculator...")
            break
        # Check operator input is valid.
        if oper not in ["+", "-", "*", "/", "**"]:
            print("Invalid operator. Please enter +, -, *, /, or ** for power.")
            continue
        
        # Perform calculation
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
            result = math.pow(num1, num2)

        #Format the result as a string with two decimal places.
        result_str = f"{num1} {oper} {num2} = {result:.2f}"
        print(result_str)

        # String Manipulation: modified result with '=>'
        fun_result = result_str.replace("=", "=>")
        print(f"{fun_result} [changed from '=' to '=>']")
        # Slicing
        print(f"result is :{result_str[8]} ")
        print(f"result is :{result_str.split('=')[1].strip()} ")

        # Use Array Data Structures: Store the result in the 'history' list.
        history.append(result_str)
        #print(history)

        # File Handling: Open the file in append mode 
        # and Save the formatted result to the file.
        with open("calc_history.txt", "a") as file:
            file.write(result_str + "\n")

    # Use Selection Structures to Code Logic and Algorithms: Handle non-numeric input error.
    except ValueError:
        print("Invalid input. Please enter numeric values.")