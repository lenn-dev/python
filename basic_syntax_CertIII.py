# print ("Hello World")
# # multiple print statements
# # triple quotes
# print("""Why is a wood chuck
#       called a wood chuck
#       if it cant chuck wood?""")

# #debug error
# # print "This should be in a braket"
# # print (please use quotes for printing string)

# #challenge1
# print("Lenn K")
# print("7 Feb 2025")
# print(""" Today is the first step in learning Python, and its going to be 
# Challenging, different to what I am used to, exciting and 
# Hopefully with very little math along the way! Lets go!!
# """)

# # challenge 2

# varName = input("Name > ")
# food = input("What is your favorite food? ")
# music = input ("What is your favorite music? >")
# location = input ("And where do you live?")
# preference = input("When you study, which way do you prefer? (study together / alone)?")
# print()
# print( varName , "'s favorite food is " , food , ", and his/her favorite music is ", music+ ".")
# print( "He/She lives in " , location , " area and He/she prefer to study ", preference ,".")

# selection statment
# Mac OS : Command + /
# num = 2 
#num = -1
# if (num > 1):
#     print("Number is greater than 1")
# print("loop ended")


# to check a number is positive
# indentation error
# num = int(input("Enter the number"))
# if (num>0):
#     print("Number is positive")
#     print("******************")
# elif (num == 0):
#     print("Number is 0")
# else:
#     print("Number is negative")
# print("loop ended")

# example of elif
# color = input("What color is your car? ")

# if color == "red":
# 	print("You have a red car!")
# elif color == "green":
# 	print("You have a green car!")
# elif color == "blue":
# 	print("You have a blue car!")
# else:
# 	print("Car not red, green or blue!")


#Example of a nested if statement

# num = float(input("Enter a number: "))

# if (num >= 0): 
#     if (num == 0):
#         print("Zero") 
#     else:
#         print("Positive number") 
# else: 
#     print("Negative number")


#Exercise 2A==================================

# 2.	Write a script to check whether the number entered by user is odd or even

# num = int(input("Enter your number"))
# if (num%2 == 0):
#       print("Number is even number")
# else:
#       print("Number is odd")

# 4. 4.	A school has following rules for the final grade based on the average of two test results:
#a.	80 or above - A
#b.	70 or above, but less than 80 - B
#c.	60 or above, but less than 70 - C
#d.	50 or above, but less than 60 - D
#e.	Below 50 - F
#. Write a python script to read in two test results marks obtained by a student and print the corresponding final grade.

# result = int(input("Your result"))

# if(result >= 80):
#       print("Your grade is A")
# elif(result >= 70 ):
#       print("Your grade is B")
# elif(result >= 60 ):
#       print("Your grade is C")
# elif(result >= 50 ):
#       print("Your grade is D")
# else:
#       print("Your grade is F")


#3.	Write a Python script to see if a value entered by the user can be divided by both 5 and 7.

# value = int(input("Enter the value"))

# if(value % 5 == 0 and value % 7 == 0):
#       print("The value can divided by both 5 and 7")
# else:
#       print("The value cannot divided by both 5 and 7")


#5.Write a python program to read the ages of 3 people and determine the oldest and the youngest among them.

# a = int(input("Enter your age "))
# b = int(input("Enter your age "))
# c = int(input("Enter your age "))

# if(a > b):
#       if( a > c):
#             if(b > c):
#                   print( a, "is oldest and", c, "is youngest")
#             else:
#                   print(a, "is oldest and", b, "is youngest")
#       else:
#             print(c, "is oldest and", b, "is youngest")            
# else:
#       if( a < c ):
#             if(b > c ):
#                   print(c, "is oldest and", a, "is youngest ")
#             else:
#                   print(b, "is oldest and", a, "is youngest")      
#       else:
#             print(b, "is oldest and", c , "is youngest")          



# 6.A student will be allowed to take up the exam only if his/her attendance is more than 75%.
#Write a python script to read the number of classes attended from the user, 
# determine whether he/she is eligible or not. Number of classes held = 50
#Hint: attendance = (no attended/no held)*100

# NumOfClasses = 50
# attendence = int(input("Enter number of attendence :"))
# percOfAtt = (attendence / NumOfClasses) * 100

# if (percOfAtt >= 75):
#       print("You are eligible for the exam")
# else:
#       print("You are Not eligible for the exam")


#7.The following table displays annual car insurance premiums based on age and gender.
#	   Age less than 25  | Age 25 or greater
# Male   |   $1,000	   |     $800
# Female |	   $700    	   |     $500
# Create a script that will calculate a person’s annual car insurance 
# after they have entered their age and gender.

# age = int(input("Enter your age"))
# gender = input("Enter your gender")

# if (age < 25  and gender == "male"):
#       print("Your annual car insurance is $1000")
# elif (age >= 25  and gender == "male"):
#       print("Your annual car insurance is $800")
# elif (age < 25  and gender == "female"):
#       print("Your annual car insurance is $700")      
# else :
#       print("Your annual car insurance is $500")


# session3
# while loop ===================
# n=0
# while n>0:
#       n=n-1
#       print(n)


# break
# n=2 일 경우 그 부분에서 실행종료됨
# n=5
# while n>0 :
#       n=n-1
#       if n== 2:
#             break
#       print(n)
# print("Loop ended")

#continue statement
# n=2 일 경우에만 print(n)이 실행되지 않고, while문 계속됨
# continue 는 stop and go back 이란 뜻이라고 이해하면 쉬움
# n=5
# while n>0 :
#       n=n-1
#       if n== 2:
#             continue
#       print(n)
# print("Loop ended")

# for loop
# for i in [2,4,5,7,9,1]: # iterble 튜플같은 자료형
#       print(i)

# nums = [2,4,5,7,9,1] #List
# for i in nums: 
#       print(i)

# fruits =["Apple", "banana","grapes"]
# for x in fruits:
#       if x == "banana":
#             continue
#       print(x)

# fstrings
# name = "john"
# age = 25

# print(f"My name is {name} and my age is {age}")



# session 4

# Exercise session3
# while/For Loops==================================================
#Complete the following programming exercises.  
# Do a screen shot of your code and paste it in the spaces below each question.

#1.Using a while loop, write a script to print first 10 natural numbers. Print each number to the screen.
# num = 10
# while (num > 0 ):
#       print(num)
#       num = num - 1 # num -= 1
# print("loop ended")

#2.Using a while loop, write a script to print first 10 natural numbers except for the number 5.

# n = 10
# while n > 0 :
#       n = n - 1
#       if (n == 5):
#             continue
#       print(n)
# print("Loop ended")

#3.Write a script to print the square of all numbers from 0 to 10.
# num = 10
# while num >= 0:
#     #print(f"{num}^2 = {num ** 2}")
#     print("squared number: ", num ** 2)
#     num -= 1



#4.Using a for loop, write a script to print first 10 natural numbers. Print each number to the screen.
#range() print 0 ~ n-1
# range(1,11)

# for i in range(10):
#       print(i)

#5.Using a for loop, write a script to print first 10 natural numbers except for the number
# for num in range(1, 11):
#     if num == 5:
#         continue
#     print(num)


#6.Using a for loop, write a script to print the square of all numbers from 0 to 10.
# for num in range(11):
#     print(f"{num}^2 = {num ** 2}")


# import math

# for num in range(11):
#     square = math.pow(num, 2)
#     print(f"The square of {num} is {square}")


#7.Write a for loop to count from 1 to 20. Can you make it count in fours? 
#Can you make it count backwards?

# for num in range(1, 21, 4):
#     print(num)

# for num in range(20, 0, -1):
#     print(num)

# for num in range(20, 0, -4):
#     print(num)



#8.	Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#a.	Hint: Use the continue statement.
# for num in range(7):
#       if num == 3 :
#             continue
#       print(num)


#9.	Write a Python program to count the number of even and odd 
#a.	numbers from a series of numbers
#numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# odd = 0
# even = 0
# for num in range(1,10):
#       if num % 2 == 0:
#            even += 1
#       else:
#             odd += 1
# print("Odd number count: ", odd)
# print("Even number count: ", even)


#10.Calculate the sum and average of first n natural numbers using:
#-	For loop and While loop

# n = int(input("Enter number"))
# sum = 0 

# for num in range(n+1):
#       sum = sum + num
# average = sum / n

# print("sum:", sum)
# print("average: ",average )      




#1
# num = 10
# while (num > 0 ):
#       print(num)
#       num = num - 1 # num -= 1
# print("loop ended")

#2
# n = 0
# while n < 10 :
#       n = n + 1
#       if (n == 5):
#             continue
#       print(n)
# print("Loop ended")

# #3
# num = 0
# while (num<11):
#       print(f"{num}^2 = {num**2}")
#       num += 1

# #7
# for num in range(1,21,4):
#       print(num)

# for num in range(1,21,-1):
#       print(num)

# #9
# even = 0
# odd = 0
# numbers=[1,2,3,4,5,6,7,8,9]
# for n in numbers:
#       if n % 2 == 0: 
#             even += 1
#       else:
#             odd += 1
# print(f"odd number count: {odd}")
# print(f"odd number count: {even}")

#EXERCISE 6=========================================
# 1. Write a program to demonstrate to get index and value of the element from the list.

# Here is a sample list you can use:

myList = ["first", "second", "third", "fourth", "fifth"]

# get (and print) the value of the second element from list.
# Note subscripts are ZERO-based:
# Your answer:
#print(myList[1])


# Now, get (and print) the index of the element with value "fourth":
# Your answer:
#print(myList[3])

# 2. Using iteration fin the list, print a Happy New Year message to 
#    all the members in the list Friends:

# Here is the list:

friends = ["John", "Frank", "Gitty", "Oliver"]

# Your answer: (print a Happy New Year message to all the friends

#for n in friends:
#    print(f"{n},Happy New Year ")

# Now, add Sam and Garry to the list, after John and before Frank, 
# then print the extended list

# Your answer:

# friends.insert(1,"Sam")
# print(friends)
# friends.insert(2,"Garry")
# print(friends)

# 3. Write a program to calculate the average of items in the list.
#    Hint:Use len() and sum() functions.
#    You can use this list or change it to your own values:

a = [5, 6, 4, 7, 2, 9, 10, 5, 6, 7, 101, 11, 51, 9]

# Your answer:
# avg = sum(a)/len(a)
# print(avg)

# 4. From the following list of numbers, write a script to 
#    remove the duplicates values.

original = [5, 6, 4, 7, 2, 9, 10, 5, 6, 7, 101, 11, 51, 9]

# Your answer:
# unique = []
# for item in original:
#     duplicate = False
#     for uniq_item in unique:
#         if uniq_item == item:
#             duplicate = True
#             break   
#     if duplicate == False:   #  not duplicate  OK
#         unique.append(item)
# print(unique)

# unique=[]
# for item in original:
#     if item not in unique:
#         unique.append(item)
# print("list with duplication removed")
# print(unique)


# seaching 
states = ["QLD", "NSW", "ACT", "VIC", "TAS", "SA", "WA", "NY"]

# found = False
# the_state = input("Enter a state: ")

# for x in states:
#     if x == the_state:
#         found = True
#         break

# if found == False:
#     print("Not a valid state")
# else: 
#     print("Valid state entered")


#session5 function=====================================

# def evenOdd(x): 
#     if(x % 2==0):
#         print("even")
#     else:
#         print("odd")

# evenOdd(2)
# evenOdd(3)

# def add(num1, num2):
#     sum = num1 + num2
#     print("The sum is",sum)

# add(1,2)

#default parameter
# def my_function(country="Norway"):
#     print("I am from "+ country)

# my_function("Australia")
# my_function()

# def add(num1,num2):
#     sum = num1+num2
#     return sum

# print("The sum is", add(7,8))

# def print_something():
#     something = input("enter the string")
#     print(something)

# print_something()


# num =int(input("Enter the number"))
# print(type(num))

# math module
# import math
# #find the square root of a number
# number=25
# result = math.sqrt(number)
# print(result)

# import math
# x=math.pi
# print(x)

# random module
# randomint
# import random
# x = random.randint(1,10)
# print(x)

# random choice
# import random
# #Generate a random integer between 1 and 100
# random_number = random.randint(1,100)
# print("Random number between 1 and 100:", random_number)
# #Choose a random item from a list of colors
# colors = ['red', 'green', 'blue', 'yellow', 'purple']
# random_color = random.choice(colors)
# print("Random color from the list", random_color)



#================================================
# Exercise Algorithms and Flowcharts
# compare 3 numbers and return biggest number 

# def biggest(a,b,c):
#     if a > b:
#         if a > c:
#             print(f"The biggest number is {a}")
#         else: 
#             print(f"The smallest number is {b}")
#     else:
#         if b < c:
#             print(f"The biggest number is {c}")
#         else:
#             print(f"The biggest number is {b}")

# print("Find the biggest number in 3 numbers")
# num1 = int(input("Please enter first number: "))
# num2 = int(input("Please enter second number: "))
# num3 = int(input("Please enter third number: "))

# print("The biggest number is ", biggest(num1,num2,num3))



#1.
# num = int(input("Enter the number"))
# if(num % 2==0):
#     print("even")
# else:
#     print("odd")


#2.
# def choose(x): 
#     if(x == "sunny"):
#         print("wear a short pants")
#     elif(x =="rainny"):
#         print("wear a rain coat")
#     elif(x =="cold"):
#         print("wear a jacket")   

# weather =input("Today is sunny or rainny, cold? ")

# choose(weather)

# 3.
# def evenOdd(x): 
#     if(x % 2==0):
#         print("even")
#     else:
#         print("odd")

# num = int(input("Enter the number"))
# evenOdd(num)

# 4. 
# def print_something():
#     something = input("enter the string")
#     print(something)

# print_something()

# 5. 
# def greeting():
#     name = input("enter your name")
#     print(f"Hello",name)

# greeting()

#6.
# def evenOdd(x): 
#     if(x % 2==0):
#         print("even")
#     else:
#         print("odd")

# num = int(input("Enter the number"))
# evenOdd(num)


#session6===========================
# file handling

#read file
# my_file = open("example.txt",'r')
# #content = my_file.read()
# #content = my_file.read(4)
# #content = my_file.readline() #list format
# content = my_file.readlines()
# print(content)
# my_file.close()


# with open("example.txt") as my_file:
#     content = my_file.read()
#     print(content)



# write in to file
# use writhe mode "w" - overwrite 
# my_file = open("example.txt","w")
# my_file.write("This is a test file1 \n")
# my_file.write("This is a test file2 \n")
# my_file.write("This is a test file3 \n")
# my_file.close()

# should open file with write mode first and store in the object
# and using the object, write the lines
# with open("example.txt","w") as file:
#     lines = ["line one\n","line two\n","line three\n"]
#     file.writelines(lines)


# append method 
# when write something in an existing txt file
# then remove previous content in txt file and overwrite the string
# if you don't want to remove it and add content
# use append method "a"
# with open("example.txt","a") as file:
#     file.write("This is the new line")

# looping over a file object
# f = open("example.txt","r")
# for line in f:
#     print(line)
# f.close()

# String=================
# str3= "123"
# str3 = int(str3) + 1 
# print(str3)

#indexing
fruit = 'banana'
# letter = fruit[1]
# print(letter)
# n = 3
# letter2 = fruit[n-1]
# print(letter2)

# Access a character in string
# replace
# s1="Hello Bob"
# print(s1)
# s2=s1.replace("Bob","Robert")
# print(s2)

# slicing
# message ='python is awesome'
# print (message[0:5])
# print (message[7:10])
# print (message[10:17])
# print (message[:])
# print (message[5:])
# print (message[:6])

# message[0] = 'J' 
# Error: str object does not support item assignment

#read string using loop
fruit = 'banananana'
# for i in range(len(fruit)):
#     print(fruit[i])
#     # print(fruit[i],end=".")

# for c in fruit:
#     print(c,end=",")

# String Library
# upper/lower letter
# greet="Hello Bob"
# lower = greet.lower()
# print(lower)
# upper = greet.upper()
# print(upper)

#serching string : find()
# fruit = "banana"
# pos = fruit.find('na') #return first position of string
# print(pos)
# aa = fruit.find('z') # if cannot find the string then return -1
# print(aa)

#seach and replace
# greet ="Hello Bob"
# newstr = greet.replace('Bob','Jane')
# print(newstr)
# newstr = greet.replace('o','x')
# print(newstr)