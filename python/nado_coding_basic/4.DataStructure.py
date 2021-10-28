"""
본 로직은 나도코딩 자료구조 파트를 따라서 작성함을 알립니다.
https://www.youtube.com/watch?v=kWiCuklohdY
"""

# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 활용방법
# 조세호씨가 몇번째 칸을 타고 있는가?
print(subway.index("조세호"))
# >> 1번째칸에 타고있음(index는 0부터 시작)

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)
#
# print(subway.pop())
# print(subway)
# => 유재석과 정형돈만 남음

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))
# => 유재석을 추가했으니 두명의 유재석이 추가되어 있는 것을 확인할 수 있음

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 리스트 안에 모든 값 삭제
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

# ==> numlist += mix_list 와 같은 기능


# 사전(dictionary) {}

cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

# print(cabinet[5]) >> KEYError
print(cabinet.get(5))  # >> 값이 없어도 None으로 반환가능
print(cabinet.get(5, "사용 가능"))  # >> 값이 없을때 default 값 설정 가능

# 사전 자료형 안에 값을 확인 하는 방법

print(3 in cabinet)  # True | 3이라는 key 값이 cabinet 안에 있는지 확인
print(5 in cabinet)  # False

# 키 값은 정수가 아닌 다른 값으로도 가능
cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"  # 기존 키 값을 다른 값으로 변형 (update)
cabinet["C-20"] = "조세호"  # 새로운 키 값을 추가 (insert)
print(cabinet)

# 간 손님
del cabinet["A-3"]  # 키 값 삭제 (delete)
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()  # cabinet 안에 존재하는 모든 값들을 삭제
print(cabinet)

# 튜플 ()
# 튜플은 list와 dictionary와 다르게 값을 추가하거나 변경을 할 수 없다.
# 변경되지 않는 값을 사용할때 사용

menu = ("돈까스", "치즈까스")  # 변경되지 않는 메뉴
print(menu)
print(menu[0])
print(menu[1])

# menu.add("생선까스") >> Occurred Error # tuple은 add라는 method가 없음

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

#  ==

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

# 셋, 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자, 둘 어느거나 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")  # 추가
print(python)

# java를 까먹은 사람
java.remove("김태호")  # 값 삭제
print(java)

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))  # 자료형태가 set이라는 것을 확인 가능

menu = list(menu)  # 메뉴의 자료 형태를 list로 변경
print(menu, type(menu))

menu = tuple(menu)  # 메뉴의 자료 형태를 tuple로 변경
print(menu, type(menu))

menu = set(menu)  # 메뉴의 자료 형태를 처음 형태인 set으로 변경
print(menu, type(menu))

# ----------------------------------------
"""
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오

조건 1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건 2: 댓글 내용과 상관 없이 무작위로 추첨히되 중복 불가
조건 3: random 모듈의 shuffle과 sample을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --

(활용 예제)
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))
"""

# Answer)
from random import shuffle, sample

id_list = [i for i in range(1, 21)]
shuffle(id_list)
win_chick = sample(id_list, 1)[0]

id_list.remove(win_chick)

shuffle(id_list)
win_coffee = sample(id_list, 3)
print(f"""-- 당첨자 발표 --
치킨 당첨자 : {win_chick}
커피 당첨자 : {win_coffee}
-- 축하합니다 --""")

# Correct Answer
from random import *

users = range(1, 21)
users = list(users)

shuffle(users)
winners = sample(users, 4)  # 4명 중에서 1명은 치킨, 3명은 커피

print("-- 당첨자 발표 --")
print(f"치킨 당첨자 : {winners[0]}")
print(f"커피 당첨자 : {winners[1:]}")
print("-- 축하합니다 --")
