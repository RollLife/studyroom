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

# 파일 입출력
score_file = open("score.txt", "w", encoding="utf8")  # score.txt를 쓰기 목적을 위한 파일로 열고 인코딩을 utf8로 맞춰준다.
print("수학 : 0 ", file=score_file)  # print는 자동 줄바꿈
print("영어 : 50", file=score_file)
score_file.close()  # 파일은 열면 항상 닫아줘야한다.

score_file = open("score.txt", "a", encoding="utf8")  # 이미 존재하는 파일에 덮어씌우기(a는 append의 의미)
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")  # write는 줄바꿈이 안되기때문에 명시적으로 작성해주어야한다.

score_file = open("score.txt", "r", encoding="utf8")  # 작성된 파일을 읽기
print(score_file.read())  # 한번에 모든 내용을 불러오기
score_file.close()

# 각각 한줄씩 읽기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())  # print는 자동줄바꾸미 되기때문에 한줄 더 줄바꿈이 되고있음.
print(score_file.readline(), end="")  # 줄바꿈 안하기
print(score_file.readline())  # 줄바꿈 안하기
score_file.close()

# 반복문을 통한 출력
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

# 리스트 형태로 저장후 출력
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")

score_file.close()

# pickle
# 프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장
# 불러올 때 또한 pickle을 사용해서 파일을 불러올 수 있다.
import pickle

profile_file = open("profile.pickle", "wb")  # pickle을 쓰기위해서는 항상 binary, encoding은 필요없음
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")  # 읽기 전용, 바이너리
profile = pickle.load(profile_file)  # 파일에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

# with
# 지금까지는 파일을 작업할때 항상 파일을 열고 닫고 했어야했음.
# 따로 close를 하지 않아도됨, 더욱 수월하게 파일처리가 가능함

import pickle

# 피클을 이용한 파일 불러오기
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

# 쓰기
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

# 읽기
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

# --------------------------------------------
"""
Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X 주차 주간보고 -
부서 : 
이름 : 
업무 요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
"""

# Answer)
for week in range(1, 51):
    with open(f"{week}주차.txt", "w", encoding="utf8") as f:
        f.write(f"- {week} 주차 주간보고 -\n")
        f.write(f"부서 : \n")
        print("이름 : ", file=f)
        print("업무 요약 : ", file=f)

# Correct Answer)
for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as f:
        f.write(f"- {i} 주차 주간보고 -\n")
        f.write(f"부서 : \n")
        f.write(f"이름 : \n")
        f.write(f"업무 요약 : ")
