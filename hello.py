# 실행하기 ctrl+option+N
print("Hello world")

# variables
# 파이썬은 코드를 위 => 아래로 순차적으로 읽는다.
a = 2
b = 3
c = a + b
c = 1
a = 4
b = 5
print(c)
print(a)
print(b)

# data type : number, text, boolean
# True/False 대문자로 꼭 쓰기
my_name ="len"
age = 12
dead = False
print("Hi my name is ",my_name)
print("and I'm",age, "years old")

# function
# def name(): 
# 파이썬은 {}없어서 함수 안에 실행문은 들여쓰기(tab) 해야 함수안에 포함됨
# 공백에 민감한 언어

def say_hello(name,age):
    print("hello", name, "how r u ?")
    print("your are", age, "years old")

say_hello("lenn",15)

def tax_calculator(salary):
    print(salary * 0.35)

tax_calculator(3500000)
tax_calculator(350)





