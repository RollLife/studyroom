"""
본 로직은 나도코딩 문자열 처리 파트를 따라서 작성함을 알립니다.
https://www.youtube.com/watch?v=kWiCuklohdY
"""

# [문자열]

sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)
# sentence3는 문자열을 길게 혹은 다양하게 표현할때 사용한다. 또한 줄바꿈 문자도 자동으로 포함해준다.

# [슬라이싱]

jumin = "990120-1234567"

print("성별 : " + jumin[7])  # jumin 변수의 8번째 부분에 존재하는 순서에 해당하는 문자를 뽑는다(처음 시작 순서가 0,1,2,3...)
print("연 : " + jumin[0:2])  # 0 부터 2 직전까지 (0, 1)
print("월 : " + jumin[2:4])  # 2 부터 4 직전까지 (2, 3)
print("일 : " + jumin[4:6])  # 4 부터 6 직전까지 (4, 5

print("생년월일 : " + jumin[:6])  # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:])  # 7번째(1)부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])  # 맨 뒤에서 7번째(1)부터 끝까지

# [문자열 처리 함수]
python = "Python is Amazing"
print(python.lower())  #
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")  # 인덱스는 파이썬에서 해당 문자의 위치 0(P),1(y),2(t),3(h),4(o),5(n) -> 5번째 위치(첫번째 n)
print(index)
index = python.index("n", index + 1)  # 두번째 n의 위치
print(index)

# 비슷한 함수 find
print(python.find("n"))  # index 함수를 썼을 때 처럼 똑같이 실행
print(python.find("Java"))  # 문자열에서 포함되지 않는 문자가 포함될 경우 -1 반환
# print(python.index("Java")) # index를 썼을때 포함되지 않는 문자를 확인할 경우 에러 발생

print(python.count("n"))  # python 변수에서 몇개의 n이 확인되었는지 확인해주는 함수

# [문자열 포맷]

print("a" + "b")
print("a", "b")

# 방법 1) %를 이용한 문자열 포맷
print("나는 %d살입니다." % 20)  # %d는 숫자만(digit)
print("나는 %s를 좋아해요." % "파이썬")  # %s는 아무 문자열(string)
print("Apple 은 % c로 시작해요." % "A")  # %c는 한가지 문자(character)
print("나는 %s살입니다." % 20)  # %s는 숫자도 가능하다.
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))  # 여러가지 문자열을 섞어 넣을때 그만큼 %s와 그 갯수만큼 늘려주면된다.

# 방법 2) {} 를 이용한 문자열 포맷
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))  # {}안에 순서를 넣음으로써 어떤 값을 먼저 넣을지 선택가능, 파란을 0, 빨간을 1에 삽입
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))  # 파란을 0에, 빨간을 1에

# 방법 3) {}과 동일하지만 변수처럼 선언하여 지정해주는 방식
print("나는 {age}색과 {color}색을 좋아해요".format(age="파란", color="빨간"))  # 변수처럼 선언 가능, 이 문자열에서만
print("나는 {age}색과 {color}색을 좋아해요".format(color="파란", age="빨간"))  # 순서 바꿔서

# 방법 4) fstring 방식, python v3.6 이상에서만 지원
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")  # 데이터 타입에 상관없이 문자열 맨 앞에 f를 붙이고 {}안에 어떤값이든 지정하여 문자열과 결합가능

# [탈출 문자]/[Escape Character)

# \n : 줄 바꿈
print("백문이 불여일견,\n 백견이 불여일타")

# \" \' : 문장 내에서 따옴표 출력
# print("저는 "나도코딩" 입니다.") 해당 방식은 문자열을 "로 감쌌기 때문에 "가 문자열 안에 포함되면 안된다.
# print('저는 '나도코딩' 입니다.') 위와 동일하게 '로 감쌌기 때문에 '가 문자열 안에 포함되면 안된다.
print("저는 '나도코딩' 입니다.")  # 올바른 방식
print('저는 "나도코딩" 입니다.')  # 올바른 방식
print("저는 \"나도코딩\" 입니다.")  # "로 감싸졌어도 문자열 내에서 큰 따옴표를 출력시키기 위한 escape 문자 \(역슬래쉬)를 붙여주면 출력가능
print('저는 \'나도코딩\' 입니다.')

# \\ : 문장 내에서 \ 출력
# print("c:\User\workspace") # \는 문자열 내에서 그냥 출력될 수 없음, \U, \w 이렇게 처리해버리기 때문
print("c:\\User\\workspace")  # \를 출력시키기 위해서는 \를 따옴표 처리하듯이 두번 입력하면 된다.

# \r : 커서를 맨 앞으로 이동
print("Red apple\rPine")  # Red apple을 먼저 적은뒤 맨 앞으로 이동하여 Pine을 적음 >> (Red )apple => Pineapple (덮어쓰기)

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")  # d 삭제 >> RedApple

# \t : 탭(네 번 space 친것과 동일한 효과지만, 한개의 문자로 인식을 한다.)
print("Red\tApple")

# ---------------------------------------------------------------------------------------
'''
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙1: http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리(nav) + 글자 갯수(5) + 글자 내 'e' 갯수(1) + "!" 로 구성(!)

예) 생성된 비밀 번호 : nav51!
'''
# ----------------------------------------------------------------------------------------

# Answer

site = "http://google.com"
uri = site.replace("http://", "")

first_dot_index = uri.index(".")
uri = uri[:first_dot_index]

until_third_index = uri[:3]
text_length = len(uri)
count_character_e = uri.count("e")

password = f"{until_third_index}{text_length}{count_character_e}!"

print(f"{site}에서 생성된 비밀번호 : {password}")
