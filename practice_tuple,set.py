# 튜플, 리스트와 다르게 변경이나 추가를 할 수 없음
#속도가 리스트보다 빠르다

#돈가스 집
menu = ("돈가스", "치즈가스")
print(menu[0])
print(menu[1])

#menu.add("생선가스") #값을 추가 및 변경x

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

# 집합 (세트)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) #중복 허용 x

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java도 할 수 있고, python을 할 수 있는 개발자)
print(java | python)
print(java.union(python)) #순서 보장 x

#차집합 (java는 할 수 있지만 python을 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

#python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 잊었어요
java.remove("김태호")
print(java)