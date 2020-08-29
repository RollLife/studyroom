"""
본 로직은 나도코딩 자료형 파트를 따라서 작성함을 알립니다.
https://www.youtube.com/watch?v=kWiCuklohdY&t=64s
"""

# [숫자 자료형]
print(5)  # >> 5 | 정수
print(-10)  # >> -10 | 음수
print(3.14)  # >> 3.14 | 실수
print(1000)  # >> 1000 | 큰 숫자
print(5 + 3)  # >> 8 | 연산
print(2 * 8)  # >> 16 | 곱연산
print(3 * (3 + 1))  # >> 12 | 다소 복잡한(?) 연산

# [문자형 자료형]
print('풍선')  # >> 풍선 |  single quotation
print("풍선")  # >> 풍선 |  double quotation
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")  # >> ㅋㅋㅋㅋㅋㅋㅋㅋㅋ | continuous string
print("ㅋ" * 9)  # >> ㅋㅋㅋㅋㅋㅋㅋㅋㅋ | 위와 같은 결과(숫자와 문자열을 조합하면 연속된 자료형의 갯수를 나타낼 수 있음)

# [Boolean 자료형]

# 참 / 거짓
print(5 > 10)  # >> False
print(5 < 10)  # >> True
print(True)  # >> True
print(False)  # >> False
print(not True)  # >> False
print(not (5 > 10))  # >> True | 5 > 10 - False => not False == True
