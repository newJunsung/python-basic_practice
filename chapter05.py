# # 리스트
# subway = ["유재석", "조세호", "박명수"]
# print(subway)
# print(subway.index("조세호"))
# print(subway.count("유재석"))

# subway.append("하하") # 리스트의 마지막에 리스트를 추가할 때
# subway.insert(1, "정형돈") # 특정 부분에 리스트를 추가할 때
# print(subway)

# print(subway.pop()) # 리스트의 마지막 부분부터 삭제

# num_list = [5,4,2,1,3,7]
# num_list.sort() # 오름차순으로 정렬
# print(num_list)
# num_list.reverse() # 역순
# print(num_list)

# mix_list = ["조세호", 20 , True] # 다양한 자료형 함께 사용 가능
# num_list.extend(mix_list) # 확장(합치기)
# print(num_list)
# num_list.clear() # 모두 지우기

# # ------------------------------------------------------------

# # 딕셔너리(사전) - 중복이 허용되지 않음
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3]) # print(cabinet.get(3))
# print(cabinet[100])
# print(cabinet.get(5, "사용가능")) # 5가 있는 지 검사, 없으면 "사용가능 반환"
# print(3 in cabinet) # True
# print(5 in cabinet) # False

# cabinet[20] = "조세호"
# print(cabinet)

# del cabinet[3] # 삭제 시
# print(cabinet)
# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items()) # 키, 값 모두 출력
# cabinet.clear() # 모든 값 초기화

# # ------------------------------------------------------------

# # 튜플 - 내용 변경이나 추가가 불가능함. 대신 속도가 리스트보다 빠름.
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# name, age, hobby = "김종국", 20 , "코딩"
# print(name, age, hobby)

# # ------------------------------------------------------------

# # 세트(집합) - 중복이 안되고, 순서 없음.
# my_set = {1, 1, 2, 2, 2, 3, 3, 3, 3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])
# # 교집합
# print(java & python)
# print(java.intersection(python))
# #합집합
# print(java | python)
# print(java.union(python))
# #차집합
# print(java - python)
# print(java.difference(python))
# #원소 추가
# python.add("김태호")
# print(python)
# #원소 삭제
# java.remove("김태호")
# print(python)

# # ------------------------------------------------------------

# # 자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# # ------------------------------------------------------------

# Quiz
# id = []
# for i in range(1, 21):
#     id.append(i)
# from random import *
# shuffle(id)
# print(id)
# print("치킨 당첨자 : " + str(id.pop()))
# print("커피당첨자 : " + str(sample(id, 3)))

from random import *

id = range(1, 21)
id = list(id)

shuffle(id)
winners = sample(id, 4)

print("치킨 딩첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))