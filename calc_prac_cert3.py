import math # 4. Use Program Library Functions:math.pow()

# Store calculation history
# 8. Use Array Data Structures:store the results of calculations in a list
history = []

# Run calculator loop
 # 7. Use Loop Structures to Code Logic and Algorithms: 
while True:
    try:
        # Get user input
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        oper = input("Choose an operator (+, -, *, /, ** for power) or type 'exit' to quit: ").strip()

        # Exit condition
        if oper.lower() == "exit":
            print("Exiting calculator...")
            break

        # Validate operator
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
        elif oper == "**":  # Added power operation
            result = math.pow(num1, num2)

        # Format and store result
        result_str = f"{num1} {oper} {num2} = {result:.2f}"
        history.append(result_str)
        print(result_str)
        
        # Save to file
        with open("calc_history.txt", "a") as file:
            file.write(result_str + "\n")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
