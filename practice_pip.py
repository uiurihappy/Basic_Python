# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# 내장 함수 : 내장이 되어있기에 import 할 필요없이 사용 가능
#input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요? ")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
#import random #외장 함수
# print(dir())
# import pickle
# print(dir())

#print(dir(random)) # random 함수의 사용가능한 함수들 출력

# lst = [1,2,3]
# print(dir(lst)) #list에서 쓸 수 있는 걸 출력

# name = "Jim"
# print(dir(name))

# 외장 함수 : 내장 함수와 다르게 직접 import를 해서 사용
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) #확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
#import os
# print(os.getcwd()) # 현재 디렉토리를 표시해라

# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir()) #glob과 비슷하게 dir목록 출력
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S")) #년도-월-일 시-분-초
# import datetime
# #print("오늘 날짜는 ", datetime.date.today())
# # timedelta : 두 날짜 사이의 간격
# today = datetime.date.today() # 오늘 날짜 저장
# td = datetime.timedelta(days = 100) # 100일 저장
# print("우리가 만난 지 100일은", today + td) #오늘부터 100일 후의 정보 출력
# Quiz)  프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

# 조건: 모듈 파일명은 byme.py로 작성

# (모듈 사용 예제)
import byme
byme.sign() 

# (출력 예제)
# 이 프로그램은 나도코딩에 의해 만들어졌습니다.
# 유튜브 : http://youtube.com
# 이메일 : nadocoding@gmail.com

