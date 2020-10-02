"""
본 로직은 나도코딩 제어문 파트를 따라서 작성함을 알립니다.
https://www.youtube.com/watch?v=kWiCuklohdY
"""

# if
# 분기 제어문
weather = "비"
# weather = "미세먼지"
# weather = "맑아요"
# weather = input("오늘 날씨는 어때요? ") # 직접 입력을 받는 method

if weather == '비' or weather == '눈':
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요.")

# temp = int(input("기온은 어떄요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지마세요.")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지마세요")

# for
# 반복 제어문
# 같은 작업을 여러번 반복 시킬때 사용

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")


# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {}".format(waiting_no))
# for waiting_no in range(5):
#     print("대기번호 : {}".format(waiting_no))
for waiting_no in range(1, 6):
    print("대기번호 : {}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{}, 커피가 준비되었습니다".format(customer))

# while
# 어떤 조건을 만족할때까지 반복


# customer = "토르"
# index = 5
#
# while index >= 1:
#     print("{}, 커피가 준비되었습니다. {} 번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")


# customer = "아이언맨"
# index = 1
# while True:  # 무한 루프
#     print("{}, 커피가 준비되었습니다. {} 번 남았어요".format(customer, index))
#     index += 1


# customer = "토르"
# person = "Unknown"
#
# while person != customer:  # customer가 토르일 경우에만 통과
#     print("{}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")
