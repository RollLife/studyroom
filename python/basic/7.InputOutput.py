"""
본 로직은 나도코딩 입출력 파트를 따라서 작성함을 알립니다.
https://www.youtube.com/watch?v=kWiCuklohdY
"""

# 표준 입출력
print("Python", "Java")  # 콤마를 이용해서 출력하면 둘 사이가 띄워져서 출력됨
print("Python" + "Java")  # 위의 로직과 같은 결과

print("python", "Java", sep=",")  # 콤마가 들어가는 부분 대신에 구분자를 넣어준다
print("python", "Java", "JavaScript", sep=" vs ")

# >> 한줄에 표현이 되어버림
print("호릴릴리", end="?")  # end : 문장의 끝을 ?로 만들어달라는 표시
print("무엇이 더 재밌을까요?")

import sys

print("python", "Java", file=sys.stdout)  # 표준 출력
print("python", "Java", file=sys.stderr)  # 표준 에러

# 시험 성적
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():  # key, value
    # print(subject, score)
    print(subject.ljust(8),  # 왼쪽 정렬(그리고 8칸 확보)
          str(score).rjust(4), sep=":")  # 오른쪽 정렬(그리고 왼쪽 4칸 확보)

# 은행 대기 순번표
# 001, 002, 003
# for num in range(1, 21):
#     print("대기번호 : " + str(num))
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))  # 값을 세자리수로 만들고 값이 없는 공간은 0으로 채우기

# # 표준 입력
# answer = input("아무 값이나 입력하세요 : ")  # 사용자의 입력값이 answer에 저장됨
# print("입력하신 값은 " + answer + "입니다.")

# 사용자 입력은 항상 문자열로 저장이 된다.
# answer가 10으로 입력을 한다고 해도 문자열 형태라는 것


# 다양한 출력 포맷
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: > 10}".format(500))
# 0: (빈공간):>(오른쪽 정렬을 하되)10(10개의 자리를 확보)하고 500을 출력

# 양수일 떈 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 첫번째 것도 -500이 되지만 양수일때는 + 500이 찍히지 않는다
# print("{0: > 10}".format(500))
# print("{0: > 10}".format(-500))

# 왼쪽 정렬하고, 빈 칸을 _로 채움
print("{0:_<+10}".format(500))
print("{0:_<-10}".format(500))  # +500이 찍히지 않는다.

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(1000000000000))
# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(1000000000000))
print("{0:+,}".format(-1000000000000))
# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수도 확보하기
# 돈이 많으면 행복하니까 빈 자리는 & 로 채워주기
print("{0:^<+30,}".format(10000000000))
print(f"{10000000000:^<+30,}")  # 같은 문장이지만 f string으로 작성
# 소수점 출력
print("{0:f}".format(5 / 3))
# 소수점 특정 자리수 까지만 표시(소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5 / 3))
print(f"{5 / 3:.2f}")  # 같은 문장이지만 f string으로 작성
