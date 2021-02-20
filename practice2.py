sentence = '나는 소년입니다.'
print(sentence)

sentence2 = "파이썬은 쉽습니다."
print(sentence2)

sentence3 = """
나는소년이고, 
파이썬은 쉬워요
"""
print(sentence3)

jumin = "990120-1234567"
print("성별 : "+ jumin[7])
print("연: "+ jumin[0:2]) #0~2 직전, 즉 0~1까지 출력
print("월: "+ jumin[2:4]) #2~3
print("일: "+ jumin[4:6]) #4~5
print("생년월일: "+ jumin[:6]) #처음부터 6직전까지

# print("뒤 7자리: "+jumin[7:14])
print("뒤 7자리: "+jumin[7:]) #7부터 끝까지
print("뒤 7자리 (뒤에서 부터): "+jumin[-7:]) #맨뒤에서 7번째부터 끝까지

#문자열 처리

python = "Python is Amazing"
print(python.lower()) #소문자로 출력
print(python.upper())
print(python[0].isupper())
print(python[0].islower())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index) #첫 번째 n의 위치
index = python.index("n", index+1)
print(index) #두 번째 n의 위치

print(python.find("Java")) #-1이 나옴 원하는 값이 나오지 않으므로

#print(python.index("Java"))

print("hi")

print(python.count("n")) #n의 갯수