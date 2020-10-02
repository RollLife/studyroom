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

temp = int(input("기온은 어떄요? "))
if 30 <= temp:
    print("너무 더워요. 나가지마세요.")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지마세요")
