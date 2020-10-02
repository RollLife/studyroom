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


# continue and break
# 반복문 내에서 해당 반복을 넘어갈 것인지(continue), 반복을 그만둘것인지 결정함(break)

# absent = [2, 5] # 결석
# for student in range(1, 11):
#     if student in absent: # 해당 값들이 있는 경우엔 반복을 진행시키지 않고 넘어감
#         continue
#     print("{}, 책을 읽어봐".format(student))

absent = [2, 5]  # 결석
no_book = [7]  # 책을 깜빡했음
for student in range(1, 11):
    if student in absent:
        continue  # 해당 값들이 있는 경우엔 반복을 진행시키지 않고 넘어감(반복 계속 진행)
    elif student in no_book:
        print("오늘 수업 여기까지. {}는 교무실로 따라와".format(student))
        break  # break는 반복문을 이 7번에서 종료를 시킴(반복 종료)
    print("{}, 책을 읽어봐".format(student))

# 한 줄 for문
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1, 2, 3, 4, 5]
print(students)
students = [i + 100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

# ---------------------------------
"""
Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭되어야 합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분) 
"""

# Answer)
from random import randint

passengers = [randint(5, 50) for _ in range(50)]
correct_list = []
for idx, passenger in enumerate(passengers):
    if 5 <= passenger <= 15:
        print(f"[O] {idx + 1}번째 손님 (소요시간 : {passenger}분)")
        correct_list.append(correct_list)
    else:
        print(f"[ ] {idx + 1}번째 손님 (소요시간 : {passenger}분)")

print(f"총 탑승 승객 수 : {len(correct_list)}분")

# Correct Answer)
from random import *

cnt = 0  # 총 탑승 승객 수
for i in range(1, 51):  # 1 ~ 50 이라는 수 (승객)
    time = randrange(5, 51)  # 5분 ~ 50분 소요 시간
    if 5 <= time <= 15:  # 5분 ~ 15분 이내의 손님 (매칭 성공), 탑승 승객 수 증가 처리
        print(f"[O] {i}번째 손님 (소요시간 : {time}분)")
        cnt += 1
    else:  # 매칭 실패한 경우
        print(f"[ ] {i}번째 손님 (소요시간 : {time}분)")

print(f"총 탑승 승객 수 : {cnt}분")
