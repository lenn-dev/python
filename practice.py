
# 사용자에게 2진수 값 받기
binary = input("2진수 값을 입력하세요 :")

# 입력받은 문자열 분할하여 역순한 리스트만들기
binary = list(reversed(binary))

# 2진수=>10진수 변환 함수정의
def BinToDec(binary):
    decimal = 0
    n = len(binary)
    for i in range(0,n,1):
        decimal = decimal + int(binary[i])* 2**i 
    print("10진수로 변환한 값은",decimal,"입니다.")    
    return(decimal)  
     
BinToDec(binary)


# vsc python input() 활성화 - vsc 표준 입력을 지원하지 않음
# run 누르지 말고 debugging 상태에서 run
# run and debug (ctrl+shift+d)

# rev = origin.reverse()
# 위 코드에서 reverse() 메소드는(지금은 함수와 같다고 생각해주세용. 자세한건 객체지향 프로그래밍을 나중에 들어보시면 이해하실 수 있으실 겁니당)
# origin 을 뒤집어주지만, origin.reverse() 자체는 None 을 반환합니당
# 그래서 reve 에 None 이 할당되는 것이고용
# 원하시는 결과를 얻기 위해선 reversed() 를 써주셔야 합니다
# rev = list(reversed(origin))

# 2진수 입력받아 10진수로 출력하는 프로그램
# 알고리즘: 1010(입력값,문자타입) => 문자열분할 (공백없는 문자는 list 사용해서 분할) 
# => 문자열 리스트 돌면서 list[n] * 2**i 해서 다 더해주면  10
