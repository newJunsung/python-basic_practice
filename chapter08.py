# # 표준 입출력
# print("python", "java", "javascript", sep=",", end="?") # seperate
# print("무엇이 더 재밌을까요?")

# import sys
# print("python", "java", "javascript", file=sys.stdout)
# print("python", "java", "javascript", file=sys.stderr)

# scores = {"수학":0, "영어":50, "코딩": 100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(4), str(score).rjust(4), sep=":")

# for num in range(1, 21): # 은행 대기순번표, 001 002 003 ~
#     print("대기번호: " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))
# print("입력하신 값은" + answer + "입니다.")

# # ----------------------------------------------------------------------

# # 다양한 출력 포맷
# print("{0: >10}".format(500))
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# print("{0:_<+10}".format(500))

# print("{0:,}".format(1000000))
# print("{0:+,}".format(1000000))
# print("{0:+,}".format(-1000000))

# print("{0:^<+30,}".format(1000000))
# print("{0:f}".format(5/3)) # float
# print("{0:.2f}".format(5/3)) # float

# # ----------------------------------------------------------------------

# # 파일 입출력
# score_file = open("score.txt", "w", encoding="utf-8") # w = write
# print("수학: 0", file=score_file)
# print("영어: 0", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf-8") # a = append
# score_file.write("과학: 80")
# score_file.write("\n코딩: 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8") # r = read
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8") # r = read
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8") # r = read
# while True:
#     line = score_file.readline()
#     if not line:
#         break;
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8") # r = read
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()

# # ----------------------------------------------------------------------

# # pickle
# import pickle
# profile_file = open("profile.pickle", "wb") # wb = write binary
# profile = {"이름": "박명수", "나이": 30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open("profile.pickle", "rb") # wb = read binary
# profile = pickle.load(profile_file) # file에 있는 정보 profile에 불러오기
# print(profile)
# profile_file.close()

# # ----------------------------------------------------------------------

# # with
# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf-8") as study_file:
#     print(study_file.read())

# # ----------------------------------------------------------------------

# # Quiz
for i in range(1, 6):
    with open("{0}주차.txt".format(i), "w", encoding="utf-8") as work:
        work.write("- {0} 주차 주간보고-\n부서 : \n이름 : \n업무 요약 : ".format(i))