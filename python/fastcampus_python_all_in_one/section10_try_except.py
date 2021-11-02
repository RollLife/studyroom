# Section 10

# linter : 코드 스타일, 문법 체크


# 런타임 프로세스에서 발생하는 예외 처리를 잘 해야함.

# SyntexError : 잘못된 문법
# if True
#     pass

# NameError : 참조변수가 없는경우
# a = 1
# print(c)

# ZeroDivisionError : 0 나누기 에러
# print(10/0)

# IndexError : 인덱스 범위 오버
# a= [1,2]
# print(a[3])

# KeyError : dictionary 에 key 참조값이 없을때 에러
# dict = {"chach": 'asd'}
# print(dict['aaa'])

# AttributeError :  모듈, 클래스에 있는 잘못된 속성 사용시에 예외
# print(time.bububu())

# ValueError:  참조값이 없을때 에러
# x = [1,2,4]
# x.remove(1)

# FileNotFounderror
# f= open("text.txt", "r")  # 해당 파일이 없음

# TypeError 맞지않는 타입이 다를 경우
# x = ""
# print(int(123)+"asdf")


# 예외처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

name = ["achapchap"]

try:
    print(name)
    # print(name / 10)
except:
    print("error")
else:
    print("asdfas")
finally:
    print("naasdf")

# 예외처리는 하지않지만 무조건 수행하는 코딩

try:
    print("Asdf")
finally:
    print("yes~")


# 계층적으로 예외처리 구문을 잘 설계해야한다.