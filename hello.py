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
# 함수 인자를 default value로 설정가능-입력값 없을 때 출력
def say_hello(name="anonymous",age=0):
    print("hello", name, "how r u ?")
    print("your are", age, "years old")

say_hello("lenn",15)

def tax_calculator(salary):
    print(salary * 0.35)

tax_calculator(3500000)
tax_calculator(350)

# return parameter
def tax_calc(money):
    print(money*0.35)

tax_calc(150000)


# return keyword
def tax_calc(money):
    return money * 0.35

def pay_tax(tax):
    print("thank you for paying",tax)
   
pay_tax(tax_calc(1500000))

# making fruit juice
# f"" 여러개의 변수를 출력하고 싶을때 format형식을 씀
# 이모지 단축키 'control' + 'command' + 'Space'
def juice(fruit):
    return f"{fruit}+🍹"
def add_ice(juice):
    return f"{juice}+🧊"
def add_sugar(iced_juice):
    return f"{iced_juice}+🍭"

juice = juice("🍎")
cold_juice = add_ice(juice)
perfect_juice =add_sugar(cold_juice)

print(perfect_juice)

# if
winner = True

if winner:
    print("Here is your money")
else: 
    print("Here is your money")

#elif
winner = 10

if winner>10:
    print("Win the game more than 10")
elif winner<10: 
    print("Win the game less than 10")
else:
    print("Win the game 10 times")