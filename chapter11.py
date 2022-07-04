# # 모듈
# import theater_module
# theater_module.price(3)
# theater_module.price_soldier(5)
# theater_module.price_morning(4)

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# # from theater_module import price, price_morning # price_soldier는 바로 못 씀.
# from theater_module import price_soldier as ps
# ps(5) # price_solider를 ps로 재명명해서 간단하게 사용할 수도 있다.

# # -----------------------------------------------------------------

# # 패키지, __all__

# import travel.thailand # 가장 마지막 부분에는 항상 모듈이나 패키지만 가능 -> class나 함수는 바로 import 불가
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from travel import * # __init__에 __all__ 작성함
# trip_to = vietnam.VietnamPackage()
# # trip_to = thailland.ThailandPackage() # 이거는 __all__에 "thailand" 작성안해서 안됨.
# trip_to.detail()


# # -----------------------------------------------------------------

# # 패키지, 모듈 위치

# import inspect
# import random
# from travel import *
# print(inspect.getfile(random))
# print(inspect.getfile(vietnam))

# # -----------------------------------------------------------------

# # 내장함수 따로 import할 필요 없이 바로 사용 가능한 함수.

# # dir: 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random
# print(dir())
# print(dir(random))

# lst = [1, 2, 3]
# print(dir(lst))
# name = "jim"
# print(dir(name))

# # -----------------------------------------------------------------

# # 외장함수 import를 해야 사용 가능한 함수
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# os : 운영체제에서 제공하는 기본 기능 (파일 생성 삭제같은 거)
# import glob
# print(glob.glob("*.py"))

# import os
# print(os.getcwd()) # 현재 디렉토리를 표시
# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제했습니다.")
# else:
#     os.mkdir(folder)
#     print(folder, "폴더를 생성했습니다.")
# print(os.listdir()) # glob과 유사하다.

# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())
# today = datetime.date.today()
# td = datetime.timedelta(days=100) # timedelta : 두 날짜 사이의 간격
# print("우리가 만난지 100일은", today + td)

# # -----------------------------------------------------------------

# # Quiz

from byme import *
sign()