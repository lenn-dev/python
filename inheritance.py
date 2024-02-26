# oop.py 에서 배운 oop class 내용 바탕으로 
# Guard Dog을 추가하기 위해 더 상위의 Dog class를 만들고
# 나머지 Guard Dog과 Puppy Dog 의 공통된 property가 서술된 Dog class 를 상속받는다.
# Guard Dog 과 Puppy Dog 의 차이는 서로 다른 method를 가진다는 것 뿐이다.
# oop.py 코드 기준으로 refactoring 해보자

# property와 데이터를 캡슐화 하는 방법
# 부모 class 의 모든 property와 method는 자식 클래스에 모두 상속됨
class Dog:
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed
    def sleep(self):
        print("zzzzz.......")

# 상속받는 방법은 class를 인자로 추가해줌
# GuardDog은 Dog 타입의 클라스라는 뜻이다.
# GuardDog 을 __init__ 메서드로 초기화 할때 name,breed 인자를 받고
# Dog 클래스의 __init__메서드에 name,breed,5 를 전달해줄 것이다.         
class GuardDog(Dog):
    def __init__(self, name, breed):
        # super()는 상속받은 Dog 클라스에 대한 접근
        # GuardDog class 밖에서부터 받은 인자값(self, name, breed)과 우리가 만든 값(5)들로 Dog.__init__()을 호출함 
        super().__init__(name,breed,5)
        # 자식 class 에서만의 임의의 property도 set 할 수 있음
        # 이 property는 Puppy와 Dog에 공유되지 않는 유일한 값이다.
        self.aggresive = True
    # 자식 class 에서만의 method 도 가질 수 있다.
    def rrrrr(self):
        print("rrrr.. stay away!")
    

class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 0.1)

        self.spoiled = True

    def woof_woof(self):
        print("Woof Woof!")
    

# usage
ruffus = GuardDog("Ruffus","Beagle")
bibi = Puppy("Bibi","Dalmatian")

ruffus.rrrrr()
bibi.woof_woof()

ruffus.sleep()
ruffus.sleep()

