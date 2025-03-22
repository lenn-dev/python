### **Presentation Script**  

**Hello everyone,**  

Today, I’ll walk you through a calculator program, explaining how each line of code meets key programming requirements. Let’s go step by step.  

>> Here's how this program works
>>  1. The user enters two numbers and selects an operator (`+`, `-`, `*`, `/`, `**`).
>>  2. The program checks if the inputs are valid and then performs the selected operation.  
>> 3. The result is displayed on the screen, with some string manipulation for formatting.  
>> 4. The calculation result is stored in the `history` list and written to the `calc_history.txt` file.  
>> 5. If the user types `"exit"`, the program terminates.


---

### 1. **Basic Language Syntax Rules**
 
- Generally, I’ve properly declared the variables `num1`, `num2`, and `oper`. I used the correct syntax and made sure the variables are clear and descriptive. The input is also converted to integers using `int()`, which is good practice for number input. I’ve used indentation correctly, and everything is case-sensitive as expected in Python.

---
### 2. Importing the math library
```python
import math
```
- First, I import the **math library**.  
- This allows us to use built-in mathematical functions, like `math.pow()`, to perform exponentiation. Although this program only supports basic operations and exponentiation, you can use this math library to perform square roots, rounding up, down, truncated values, factorials, trigonometric functions, and logarithmic calculations.
- This satisfies **Requirement 4: Use Program Library Functions**.  

---

### 3. Creating a history list to store past calculations
```python
history = []
```
- Here, we **initialize an empty list called `history`**.  
- This will store previous calculations so it can be retrieved later if needed.  
- Since lists (or arrays) allow us to store multiple values, this fulfills **Requirement 8: Use Array Data Structures**.  

---

### **4. Starting an infinite loop to run the calculator continuously**  
```python
while True:
```
- We enter a **while loop** to keep the calculator running until the user decides to exit.  
- This satisfies **Requirement 7: Use Loop Structures to Code Logic and Algorithms**.  
---

#### **4. Handling user input with exception handling**  
```python
try:
```
- We wrap our code inside a `try` block.  
- This helps us catch errors, such as entering non-numeric values, instead of crashing the program.  
- This contributes to **Requirement 6: Use Selection Structures to Code Logic and Algorithms**.  

---
### Taking the inputs from user 
#### **5. Getting the first number from the user**  
```python
num1_input = input("Enter first number or type 'exit' to quit: ").strip()
```
- The user is prompted to enter a number or type "exit" to quit.  
- We use `.strip()` to remove extra spaces, ensuring cleaner input handling.  
- This satisfies **Requirement 10: Perform String Manipulation**.  

---

#### **6. Handling exit condition**  
```python
if num1_input.lower() == "exit":
    print("Exiting calculator...")
    break
```
- If the user types "exit", we convert it to lowercase using `.lower()` to handle case variations.  
- We then **break** out of the loop, stopping the program.  
- This is an example of **Requirement 6: Use Selection Structures**.  

---

#### **7. Converting user input to an integer**  
```python
num1 = int(num1_input)
```
- The input is converted from a string to an integer using `int()`.  
- This demonstrates **Requirement 2: Use Data Types, Operators, and Expressions**.  

#### **8. Getting the Second number from the user**  block is the same as first one.

---
#### **9. Asking the user for an operator**  
```python
oper = input("Choose an operator (+, -, *, /, ** for power) or type 'exit' to quit: ").strip()
```
- The user is prompted to choose an arithmetic operator.  
- Using `.strip()` ensures clean input.  
- This is another example of **Requirement 10: Perform String Manipulation**.  

---

#### **10. Handling exit condition for the operator**  
```python
if oper.lower() == "exit":
    print("Exiting calculator...")
    break
```
- If the user enters "exit", we terminate the program.  
- This satisfies **Requirement 6: Use Selection Structures**.  

---

#### **11. Validating the operator input**  
```python
if oper not in ["+", "-", "*", "/", "**"]:
    print("Invalid operator. Please enter +, -, *, /, or ** for power.")
    continue
```
- We check whether the user entered a valid operator.  
- If the input is invalid, we display an error message and restart the loop.  
- This is a classic example of **Requirement 6: Use Selection Structures**.  

---

#### **12. Performing the calculation**  
```python
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
```
- Here, we use **if-elif-else** statements to determine the correct operation.  
- The `math.pow()` function is used for exponentiation, showcasing **Requirement 4: Use Program Library Functions**.  
- This entire block satisfies **Requirement 6: Use Selection Structures**.  

---

#### **13. Formatting the result string**  
```python
result_str = f"{num1} {oper} {num2} = {result:.2f}"
```
- We use an **f-string** to format the result and display it with two decimal places.  
- This is an example of **Requirement 2: Use Data Types, Operators, and Expressions**.  

---

#### **14. Modifying the result string**  
```python
fun_result = result_str.replace("=", "=>")
print(f"{fun_result} (changed from '=' to '=>')")
```
- We use `.replace()` to modify the output format.  
- This is an example of **Requirement 10: Perform String Manipulation**.  

---

#### **15. Extracting part of the result using slicing**  
```python
print(f"result is :{result_str[7:]}")
```
- We extract and display only the numerical result using slicing. 
- This is another example of **Requirement 10: Perform String Manipulation**.  

---

#### **16. Storing the result in a list**  
```python
history.append(result_str)
```
- The calculated result is added to our history list.  
- This satisfies **Requirement 8: Use Array Data Structures**.  

---

#### **17. Writing the result to a file**  
```python
with open("calc_history.txt", "a") as file:
    file.write(result_str + "\n")
```
- The result is saved to a file in append mode.  
- This demonstrates **Requirement 9: Perform File Handling (Read and Write)**.  

---

#### **18. Handling non-numeric input errors**  
```python
except ValueError:
    print("Invalid input. Please enter numeric values.")
```
- If the user enters non-numeric input, the program displays an error message instead of crashing.  
- This is an example of **Requirement 6: Use Selection Structures**.  

---

### **Conclusion**  
This calculator program is a great example of how fundamental programming concepts come together. It uses loops, conditions, functions, data structures, and file handling to create a simple yet functional tool. Thanks for listening!  
