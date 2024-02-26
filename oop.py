
# oop 에서 가장 시작점이 class 만들기
class Puppy:
    
    # class 안의 함수를 method 라고 함 
    # initialising method 이름은 __이름__ 형식으로 씀

    # set the data
    def __init__(self,name,breed):
        # print(self) #<__main__.Puppy object at 0x109108890>
        self.name = name
        self.age = 0.1
        self.breed = breed
    
    # access the data 
    # class 데이터를 별도 method에서 접근가능
        
    # def __str__(self):
    #     return "Hello"
    
    def introduce(self):
        # class 안의 method가 class 안의 다른 method 호출가능
        self.woof_woof()
        print(f"My name is {self.name} and I am {self.breed} baby")
        self.woof_woof()

    def woof_woof(self):
        print("Woof Woof!")    

ruffus = Puppy("Ruffus","Beagle")
bibi = Puppy("Bibi","Dalmatian")
# method 의 argument 는 첫번째 인자로 자기자신을 참조함
# __init__메서드 print(self) 결과값과  아래 ruffus 결과값에서 같은 주소값을 같은 것을 보면 알수 있음.
# print(ruffus) #<__main__.Puppy object at 0x109108890>
# print (ruffus.name, ruffus.age,ruffus.breed)
# print (bibi.name, bibi.age,bibi.breed)

# print (ruffus,bibi) # class 를 프린트 하면 그 안의 모든 메서드를 호출하기 때문에 결과값이 Hello Hello
ruffus.introduce()
bibi.introduce()