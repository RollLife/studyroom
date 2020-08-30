"""
본 로직은 나도코딩 연산자 파트를 따라서 작성함을 알립니다.
https://www.youtube.com/watch?v=kWiCuklohdY&t=64s
"""

# [연산자]

# 연산기호(덧셈, 뺄셈, 곱셈, 나눗셈)
print(1 + 1)  # 2
print(3 - 2)  # 1
print(5 * 2)  # 10
print(6 / 3)  # 2

# **(제곱), %(나머지), //(몫)
print(2 ** 3)  # 제곱 2^3= 8
print(5 % 3)  # 나머지 2
print(10 % 3)  # 나머지1
print(5 // 3)  # 몫 1
print(10 // 3)  # 몫 3

# >, < , >=, <=
print(10 > 3)  # True
print(4 >= 7)  # False
print(10 < 3)  # False
print(5 <= 5)  # True

# ==
print(3 == 3)  # True | == 같다(등호의 개념)
print(4 == 2)  # False
print(3 + 4 == 7)  # True

# !=
print(1 != 3)  # True | != 같지 않다
print(not (1 != 3))  # False | 1 != 3 => True , not True == False

# and
print((3 > 0) and (3 < 5))  # True
print((3 > 0) & (3 < 5))  # True

# or
print((3 > 0) or (3 < 5))  # True
print((3 > 0) | (3 < 5))  # True (백 스페이스 밑에 있는 기호를 Shift 누르고 입력하면 된다, 영어로는 pipe)

# multi operator
print(5 > 4 > 3)  # True
print(5 > 4 > 7)  # False
