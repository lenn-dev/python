# 실행하기 ctrl+option+N
# 전체 주석처리 ''' '''
# print("Hello world")

# variables
# 파이썬은 코드를 위 => 아래로 순차적으로 읽는다.
'''a = 2
b = 3
c = a + b
c = 1
a = 4
b = 5
print(c)
print(a)
print(b)'''

# data type : number, text, boolean
# True/False 대문자로 꼭 쓰기
'''my_name ="len"
age = 12
dead = False
print("Hi my name is ",my_name)
print("and I'm",age, "years old")'''

# function
# def name(): 
# 파이썬은 {}없어서 함수 안에 실행문은 들여쓰기(tab) 해야 함수안에 포함됨
# 공백에 민감한 언어
# 함수 인자를 default value로 설정가능-입력값 없을 때 출력
'''def say_hello(name="anonymous",age=0):
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
   
pay_tax(tax_calc(1500000))'''

# making fruit juice
# f"" 여러개의 변수를 출력하고 싶을때 format형식을 씀
# 이모지 단축키 'control' + 'command' + 'Space'
'''def juice(fruit):
    return f"{fruit}+🍹"
def add_ice(juice):
    return f"{juice}+🧊"
def add_sugar(iced_juice):
    return f"{iced_juice}+🍭"

juice = juice("🍎")
cold_juice = add_ice(juice)
perfect_juice =add_sugar(cold_juice)

print(perfect_juice)'''

# if
'''
winner = True

if winner:
    print("Here is your money")
else: 
    print("Here is your money")
'''

#elif
'''
winner = 10

if winner>10:
    print("Win the game more than 10")
elif winner<10: 
    print("Win the game less than 10")
else:
    print("Win the game 10 times")
'''


# and/or
# 음주나이 계산기 
# 인풋은 print 와 다른 기능, 입력했을 때 사용자 response를 기다림
# 실행시키면 입력이 들어올때까지 실행이 멈추지 않음 
# 입력값이 무엇이든 정수로 바꿔주도록 int()함수 쓰기
'''
age = int(input("How old are you?"))
if (age < 18):
    print("You can't drink.")
elif age > 18 and age <35:
    print("You have free beer!")
elif age == 60 or age == 70:
    print("You have special deal!!")
else:
    print("Go ahead")
'''
# vscode에서 input()함수 키보드활성화지원이 안됨 
# => Run and Debug 
# => Python File Debug the currently active python file 클릭한 후 
# 디버그하면 실행됨 


# python standard library : 
    # print,input은 builtin되어 있지만, 다른 많은 라이브러리 함수를 쓰려면 import해줘야함
    # 모든 함수가 포함되어 있다면 엄청 느려질것이기 때문
    # random module에 있는 randint()함수를 사용할 것이다.
    
# while
# python casino
'''
from random import randint

print("Welcome to python casino")
pc_choice = randint(1,50) #랜덤넘버 사용하기

playing = True
while playing:
    user_choice = int(input("Choose number.(1-50):"))
    if user_choice == pc_choice:
        print("You won!")
        playing = False
    elif user_choice > pc_choice:
        print("Lower!")
    elif user_choice < pc_choice:
        print("Higher!")
'''
# Methods
name = "lenn"
print(name.capitalize())
print(name.startswith("l"))
print(name.endswith("l"))

# 파이썬 자료구조 3가지 : Lists,Tuples,Dicts       
# Lists[] : mutable , has many methods
days_of_week =["Mon","Tue","Wed","Tur","Fri"]

print(days_of_week[2])
print(days_of_week[-1])
print(days_of_week[-3])

print(days_of_week.count("Wed"))
days_of_week.insert(5,"Sat")
print(days_of_week)
days_of_week.append("Sun")
print(days_of_week)
days_of_week.reverse()
print(days_of_week)
days_of_week.remove("Mon")
print(days_of_week)
days_of_week.clear()
print(days_of_week)


# Tuples() : immutable, not much methods
days_of_week =("Mon","Tue","Wed","Tur","Fri")


# Dicts{} : key + value
player ={
    "name" : "lenn",
    "age": 12,
    "alive": True,
    "fav_food":["pizza","hamburger"]
}

print(player)
print(player.get("fav_food"))
print(player["fav_food"])
player['xp']=1500
print(player)
player['fav_food'].append("noodles")
print(player["fav_food"])


from requests import get
# for loop
# URL Formatting
websites = (
    "facebook.com",
    "tiktock.com",
    "https://airbnb.com",
    "google.com",
    # "https://twitter.com"
)
# for website in websites:
#     if website.startswith("https://"):
#         print(website)
#     else:
#         print("https://",website)

# Requests
# python standard library
# https://docs.python.org/3/library/index.html
# pypi - other python libraries that is not included in standard libraray
# https://pypi.org/search/ 
# requests 는 python 코드에서 웹사이트로 request 를 보낼 수 있게 해줌
# https://pypi.org/project/requests/
# 터미널명령어 pip3 install requests
# if not
result = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    # print(response.status_code)
    # response 결과값 확인: 아래 사이트
    # https://developer.mozilla.org/ko/docs/Web/HTTP/Status
    if response.status_code == 200:
        result[website] = "OK"
    else:
        result[website] = "FAILED"

print(result)
