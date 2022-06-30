# #문자열
# sentence = '나는 소년입니다'
# sentence2 = "파이썬은 쉬워요"
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """

# print(sentence)
# print(sentence2)
# print(sentence3)

# # ------------------------------------------

# # 슬라이싱
# gildong = "990120-1234567"
# print("성별 : " + gildong[7]) # 1
# print("연도 : " + gildong[0:2]) #0부터 2직전까지 99
# print("생년월일 : " + gildong[:6]) # 처음부터 6직전까지 990120
# print("뒤 7 자리 : " + gildong[7:]) # 7부터 끝까지
# print("뒤에서부터 7자리 : " + gildong[-7:])

# # ------------------------------------------

# # 문자열 처리
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n") # index는 찾고 싶은 값이 없으면 오류를 발생시킴.
# print(index)
# index = python.index("n", index + 1) # 2번째 n 위치 찾기
# print(index)

# print(python.find("n")) # find는 index와 달리, 찾고 싶은 값이 없으면 -1을 반환해줌

# print(python.count("n")) # n의 개수

# # ------------------------------------------

# # 문자열 포맷
# #방법 1
# print("나는 %d살 입니다." % 20) # decimal
# print("나는 %s를 좋아해요." % "파이썬") # string
# print("Apple은 %c로 시작해요." % "A") # character
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# #방법 2
# print("나는 {}살 입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

# #방법 3
# print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간"))

# #방법 4(v3.6 이상)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")

# # ------------------------------------------

# # 탈출문자
# print("백문이 불여일견,\n백견이 불여일타")
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")

# print("C:\\Users\\User\\Desktop") # \\: '\'로 출력됨.
# print("Red Apple\rPine") # \r: 커서를 맨 앞으로 이동
# print("Redd\bApple") # \b: 백스페이스 (한 글자 삭제)
# print("Red\tApple") # \t: tab키와 동일

# # ------------------------------------------
# Quiz
site = "http://naver.com"
site = site.split("//")[1] # site.replace("http://", "") # 규칙 1
site = site.split(".")[0] # site[:site.index(".")] # 규칙 2
length = len(site)
countE = site.count("e")

if(length >= 3):
    passwd = site[:3] + str(length) + str(countE) + "!"
else:
    passwd = site + str(length) + str(countE) + "!"

print("{1}의 비밀번호는 {0}입니다.".format(passwd, site))