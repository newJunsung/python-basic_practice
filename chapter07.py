# # 함수, 전환값과 반환값
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money):
#     print("입슴이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if(balance < 0):
#         print("출금이 불가능합니다. 잔액은 {0}원입니다.".format(balance - money))
#         return balance
#     else:
#         print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
#         return balance-money

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# open_account()
# balance = 0
# balance = deposit(balance, 1500)
# balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))

# # ---------------------------------------------------------------------------

# # 기본값, 키워드값
# def profile(name, age = 17, main_lang = "파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")
# profile("유재석")
# profile("김태호")
# profile(name="유재석", main_lang="자바", age=20)
# profile(main_lang="자바", age=20, name="김태호")

# # ---------------------------------------------------------------------------

# # 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "python", "java", "c", "c++", "c#", "javascript")
# profile("김태호", 25, "kotlin", "Swift")

# # ---------------------------------------------------------------------------

# # 지역변수와 전역변수
# gun = 10 # 전역변수

# def checkpoint(soldiers):
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# gun = checkpoint_ret(gun,2)
# print("남은 총 : {0}".format(gun))

# # ---------------------------------------------------------------------------

#Quiz
from math import *
def std_weight(height, gender):
    heightCm = height / 100
    if(gender == "남자"):
        weight = round(heightCm ** 2 * 22, 2)
    else:
        weight = round(heightCm ** 2 * 21, 2)
    return weight

height = 175
gender = "남자"
weight = std_weight(height, gender)
print("키 {0}cm {1}의 표준 체중은 {2} 입니다.".format(height, gender, weight))