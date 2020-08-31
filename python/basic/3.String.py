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
