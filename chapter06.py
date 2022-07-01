# # if
# weather = input("오늘 날씨는 어때요? ")
# if(weather == "비" or weather == "눈"):
#     print("우산을 챙기세요")
# elif(weather == "미세먼지"):
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없어요.")

# temp = int(input("기온은 어때요? "))
# if 30<=temp:
#     print("더워요. 나가지 마세요")
# elif 10 <= temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

# # ---------------------------------------------------

# # for
# for waiting_no in [0,1,2,3,4]:
#     print("대기번호: {0}".format(waiting_no))
# #for waiting_no in range(0): # 0~4
# #    print("대기번호: {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# # ---------------------------------------------------

# # while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")

# customer = "토르"
# person = "Unknown"
# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

# # ---------------------------------------------------

# # continue & break
# absent = [2, 5] # 결석
# no_book = [7]
# for student in range(1, 11):
#     if(student in absent):
#         continue
#     elif(student in no_book):
#         print("오늘 수업 어기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# # ---------------------------------------------------

# # 한 줄 for
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am Groot"]
# # students = [len(i) for i in students]
# students = [i.upper() for i in students]
# print(students)

# # ---------------------------------------------------

# Quiz
from random import *
count = 0
for i in range(1, 51):
    spendTime  = randint(5, 50)
    matching = " "
    if(spendTime <=15 and spendTime >= 5):
        matching = "0"
        count += 1
    print("[{2}] {0}번째 손님 (소요시간 : {1})".format(i, spendTime, matching))
print("총 탑승 승객 : ", count, "분")