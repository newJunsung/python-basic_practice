# # 기본연산자
# print(1 + 1)
# print(3 - 2)
# print(9 * 3)
# print(10 / 5)

# print(2 ** 3) # 2^3 = 8
# print(5 % 2) # 5/2의 나머지 1
# print(5 // 2) # 5/2의 몫 2

# print(10 > 3) # True
# print(10 >= 100) # False

# print(3 == 3)
# print(3 != 3) # print(not(3==3))

# print((3>0) and (3<5)) # print((3>0) & (3<5))
# print((3>0) | (3>5)) #print((3>0) | (3>5))

# print(5>4>3)
# print(5>4>7)

# # -----------------------------------------------------

# # 숫자 처리 함수
# print(abs(-4)) #절대값
# print(pow(4,2)) # n승 제곱 4^2
# print(max(5, 12)) # 최대값
# print(min(5,12)) # 최소값

# print(round(3.1)) #반올림
# print(round(3.78)) #반올림
# from math import * #숫자 라이브러리
# print(floor(4.87)) #내림
# print(ceil(4.11)) #올림
# print(sqrt(81)) #제곱근

# # -------------------------------------------------------------

# # 랜덤 라이브러리
# from random import *
# print(random()) #0.0~1.0 미만의 랜덤 값 생성
# print(random() * 10) #0.0~10.0 미만의 랜덤 값 생성
# print(int(random() * 10 + 1)) #1~11 미만의 랜덤 정수 값 생성

# print(randrange(1, 46)) #1~46 미만의 랜덤 정수 값 생성
# print(randint(1,45)) #1~45 이하의 랜덤 정수 값 생성

# # -----------------------------------------------------------------
# Quiz
from random import *

studyDay = randrange(4, 29) # randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월", studyDay, "일로 선정되었습니다.")
#print("오프라인 스터디 모임 날짜는 매월" + str(studyDay) + " 일로 선정되었습니다.")