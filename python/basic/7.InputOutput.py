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

# 표준 입력
answer = input("아무 값이나 입력하세요 : ")  # 사용자의 입력값이 answer에 저장됨
print("입력하신 값은 " + answer + "입니다.")

# 사용자 입력은 항상 문자열로 저장이 된다.
# answer가 10으로 입력을 한다고 해도 문자열 형태라는 것
