# 표준 입출력
# print("Python","Java", sep = ",", end = "?") #end의 의미는 문장의 끝을 "?"으로 바꾼다.
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file = sys.stdout)
# print("Python", "Java", file = sys.stderr)

#시험 성적
# scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep = ":") # ljust: 과목의 8칸 공간을 만들고 왼쪽으로 정렬

#은행 대기순번표
#001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호 : "+ str(num).zfill(3)) #3 크기의 공간을 만들고 공간이 없는 부분은 0으로 채운다.

# answer = input("아무 값이나 입력하세요 : ")
# #print("입력하신 값은 "+ str(answer) + "입니다")
# print(type(answer)) #항상 숫자를 입력해도 문자열로 저장된다.

# 출력 포맷
# 빈자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: > 10}".format(500)) # 총 10자리의 공간을 확보하고 오른쪽으로 정렬하여 출력한다.
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(-500))

# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(1000000000))
# # 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
# print("{0:+,}".format(1000000000))
# print("{0:+,}".format(-1000000000))
# # 3자리 마다 콤마를 찍어주기, 부호도 붙이기, 자릿수 확보하기
# # 돈이 많으면 좋으니 빈자리는 ^로 채워주기
# print("{0:^<+30,}".format(10000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# #소수점 특정 자리수까지만 표시
# print("{0:.2f}".format(5/3))

# 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end = "") # 줄별로 읽기 동작, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(),end = "")
# print(score_file.readline(),end = "")
# print(score_file.readline(),end = "")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line: #라인이 없을 경우 반복문 탈출
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() #list 형태로 저장
# for line in lines:
#     print(line, end = "")

# score_file.close()

# pickle: 프로그램 상에서 데이터를 파일 형태로 저장해주는 것
import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with open("profile.pickle", "rb") as profile_file: # profile_pickle을 열어서 profile_file 에 저장 후
#     print(pickle.load(profile_file)) # profile_file을 읽어와 load한다.

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간 보고 -
# 부서 : 
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건: 파일명은 "1주차.txt", "2주차.txt", ... 와 같이 만듭니다.

# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding='"utf8') as report_file:
#         report_file.write("- {0} 주차 주간 보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")