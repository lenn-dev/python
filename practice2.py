# time 모듈 등록
# 1970-01-01 00:00:00 이후에 현재까지 경과한 시간을 초 단위로 반환
from time import time

# StopWatch 클래스 설계
class StopWatch:

    # 초기자 메소드
    def __init__(self, startTime = time(), endTime = 0, elapsedTime = 0 ):
        # 데이터필드 startTime, endTime을  private 으로 접근제한
        # 현재시간으로 startTime을 초기화하는 생성자
        self.__startTime = startTime
        self.__endTime = endTime
        self.__elapsedTime = elapsedTime

    # 현재시간으로 startTime 재설정하는 start()메소드
    def start(self) :
        self.__startTime = time()

    # 현재시간을 endTime으로 설정하는 stop()메소드    
    def stop(self) :
        self.__endTime = time()

    # StopWatch 시간 초기화
    def reset(self):
        self.__startTime = 0
        self.__elapsedTime = 0
    
    # startTime 접근자(getter) 
    def get_startTime(self) :
        return self.__startTime

    # endTime 접근자(getter) 
    def get_endTime(self) :
        return self.__endTime

    # 스톱워치의 경과시간을 밀리초 단위로 반환하는 getElapedTime() 메소드
    def getElapsedTime(self):
        elapsedTime = self.__elapsedTime
        # start부터 stop까지 걸린 시간을 밀리세컨으로 elapsedTime 변수에 저장
        elapsedTime +=((self.__endTime - self.__startTime) * 1000)
        return elapsedTime
 
# StopWatch 클래스 활용
def count_num():
    # 참조변수 = 클래스 인스턴스 생성
    x = StopWatch()
    # 클래스에 있는 start() 메소드 호출
    x.start()
    # sum 변수 초기화
    sum = 0 
    # 1 부터 100,000,000 까지 숫자를 더하기
    for i in range(1 , 100000000):
        sum += i
    # stop()메소드 호출    
    x.stop()
    print("1부터 100,000,000까지 더하는데 걸린 실행시간은", x.getElapsedTime(),"밀리 초입니다.")
    x.reset()
    
count_num()



