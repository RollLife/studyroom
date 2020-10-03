"""
본 로직은 나도코딩 함수 파트를 따라서 작성함을 알립니다.
https://www.youtube.com/watch?v=kWiCuklohdY
"""


# def (함수 선언)
# 함수는 특정 부분의 연산이나 작업들을 미리 정의 해두고 호출할때 해당 작업을 실행 할 수 있게 해준다.


def open_account():  # 함수 정의
    print("새로운 계좌가 생성되었습니다.")


open_account()  # 함수 호출


# 전달값과 반환값

def deposit(balance, money):  # 잔액과 입금된 돈을 전달받음
    print("입금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance + money))
    return balance + money  # 잔액과 입금된 돈을 합쳐서 현재 통장에 있는 돈을 반환함


def withdraw(balance, money):  # 출금
    if balance >= money:  # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {} 원입니다.".format(balance))
        return balance


def withdraw_night(balance, money):  # 저녁에 출금
    commission = 100  # 수수료 100원
    return commission, balance - money - commission


balance = 0  # 잔액
balance = deposit(balance, 1000)  # 함수 호출 및 전달값과 반환값을 전달 받음
print(balance)

# balance = withdraw(balance, 2000)  # 출금 불가능
# balance = withdraw(balance, 500)  # 출금

commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))


# 기본값(default)
def profile(name, age, main_lang):
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 {2}" \
          .format(name, age, main_lang))


# 현재 이 값에 경우는 서로 다른 언어, 다른 사람, 공통정이 없는 사람들에 대한 분류
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")


# 같은 학교 같은 학년 같은 반 같은 수업
def profile(name, age=17, main_lang="파이썬"):  # 기본값 정의
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 {2}" \
          .format(name, age, main_lang))


# 다른 인자값에 미리 기본값이 선언이 되어있다면 굳이 지정하지 않아도된다. 물론 지정해도 상관은 없다.
profile("유재석")
profile("김태호")


# 키워드 값 (keyword)

def profile(name, age, main_lang):
    print(name, age, main_lang)


# 함수에서 선언된 매개변수의 값이 있다면 이렇게 키워드값을 선언해서 작성을 해준다면 순서가 뒤죽박죽이어도 함수를 선언하여 사용할 수 있다.
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", name="김태호", age=25)


# 가변인자를 사용한 함수호출

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 {0}\t나이 : {1}\t".format(name, age), end=" ")  # print 마지막에 end 키워드 값에 " "이런식으로 전달하면 줄바꿈없이 출력함
    print(lang1, lang2, lang3, lang4, lang5)


profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")  # 매번 이렇게 빈값을 작성시켜줘야함


# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Kotlin") # 만약 할줄아는 언어가 있다면 lang6을 또 추가시켜서 만들어줘야함


def profile(name, age, *language):  # *language는 내가 놓고 싶은 만큼 인자를 놓을 수 있다.
    print("이름 {0}\t나이 : {1}\t".format(name, age), end=" ")  # print 마지막에 end 키워드 값에 " "이런식으로 전달하면 줄바꿈없이 출력함
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")  # 한가지 인자가 더 늘어났지만 사용에는 문제가 없다.
profile("김태호", 25, "Kotlin", "Swift")  # 추가 가변인자를 두개밖에 사용하지 않지만 같은 함수를 사용한다.

# TIP) 서로 다른 갯수의 인자를 사용할때엔 *{variable} 을 통해 가변인자를 사용할 수 있다.


# 지역변수와 전역변수
# 지역변수 : 함수 내부에서만 선언, 사용이 가능
# 전역변수 : 프로그램 내에 어느 공간에서든지 사용 가능한 변수


gun = 10

# >> 지역변수
# def checkpoint(soldiers):  # 경계근무
#     gun = gun - soldiers  # 에러발생, gun 변수는 함수내에서 선언이 돼지도 않았는데 사용하고 있다고 에러 발생함(함수 밖에 있는 gun은 불러오지 못한다)
#     print("[함수 내] 남은 총 : {0}".format(gun))
#
#
# print("전체 총 : {}".format(gun))
# checkpoint(2)  # 2명이 경계 근무 나감
# print("남은 총 : {}".format(gun))

gun = 10


# >> 전역변수
# 가급적 전역변수는 사용하지 않는 편이 좋다.
# 프로그램 내에 퍼포먼스를 떨어뜨리기 떄문
def checkpoint(soldiers):  # 경계근무
    global gun  # 전역 공간에 있는 gun을 사용함
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


print("전체 총 : {}".format(gun))
checkpoint(2)  # 2명이 경계 근무 나감
print("남은 총 : {}".format(gun))

gun = 10


# 전역 변수 대신에 함수를 선언하여 해당 값을 대신 전달하는 방법을 사용
def checkpoint_ret(gun, soldier):
    gun = gun - soldier
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {}".format(gun))
gun = checkpoint_ret(gun, 2)  # 2명이 경계 근무 나감
print("남은 총 : {}".format(gun))

# ----------------------------
"""
Quiz) 표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중
(성별에 따른 공식)
 남자 : 키(m) x 키(m) x 22
 여자 : 키(m) x 키(m) x 21
 
조건1: 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
조건2: 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
"""


# Answer)
def std_weight(height, gender):
    gender_value = gender
    if gender_value == "여자":
        gender_value = 21
    else:
        gender_value = 22
    print("키 %scm %s의 표준 체중은 %.2fkg 입니다." % (height, gender, height * height * gender_value / 10000))


std_weight(175, "남자")
std_weight(160, "여자")


# Correct Answer)
def std_weight(height, gender):  # 키 m단위 (실수), 성별 "남자 / "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21


height = 175  # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)  # 소숫점 2자리까지
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
