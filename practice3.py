#방법 1
# print("나는 %d 살 입니다." % 20)
# print("나는 %s 을 좋아해요." % "파이썬")
# print("Apple 은 %c로 시작해요." % "A")
# %s
# print("나는 %s 살 입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

#방법 2
# print("나는 {}살 입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

#방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color= " 빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

#방법 4 (v3.6 이상 가능)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")

#탈출 문자
# \n: 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타")
 # \" \' : 문장 내에서 따옴표로 사용 가능
 # 저는 "나도 코딩"입니다.
# print("저는 '나도 코딩'입니다.")
# print('저는 "나도 코딩"입니다.')
# print("저는 \"나도 코딩\" 입니다.")

# \\ : 문장 내에서는 하나의 \로 바뀐다.
# print("c:\\Users\\차윤범\\Desktop\\Python>")

# \r: 커서를 맨 앞으로 이동
#print("Red Apple\rPine")

# \b: 백스페이스(한글자 삭제)
# print("Redd\bApple")

# \t : 탭
# print("Red\tApple")

#Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

#예) www.naver.com
#규칙1 : http:// 부분은 제외  => naver.com
#규칙2 : 처음 만나는 점(.) 이후 부분ㅂ은 제외 => naver
#규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#(nav)  (5) (1) (!)
#생성된 비밀번호 : nav51!

# url = "http://daum.com"
url = "http://google.com"
my_str = url.replace("http://", "") #규칙 1
#print(my_str)
my_str = my_str[:my_str.index(".")] #규칙 2
#my_str에서 처음부터 .의 직전까지 값을 받는다. my_str[0:5] -> 0~5 직전까지.(0,1,2,3)
#print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))
