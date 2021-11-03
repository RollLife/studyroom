# section7
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# user1.name 등등 각각의 네임스페이스의 변수

# 쿨래스 -> 객체화
# 인스턴스 : 클래스를 직접 선언하는것


# 네임스페이스 :  객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재(__dict__ 처럼)

# self의 이해
# 클래스 메소드

class SelfTest:
    def function1():
        print("function1_ called!")

    def function2(self):
        print("function2_called")


self_test = SelfTest()
# self_test.function1()
SelfTest.function1()  # class method
self_test.function2()  # instance method 각자의 네임스페이스에 있기때문에 선언 가능


# self 여러클래스를 공유하는 인스턴스 함수라고 생각하면된다. 그런데 이제 좀더 편하게 부르기 위해서 공통해서 self로 잡는것

class TestClass:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        self.name = name
        TestClass.stock_num += 1

    def __del__(self):
        # 해당 메소드는 클래스가 종료될때 호출되는 메소드
        TestClass.stock_num -= 1


# 이렇게 클래스안에 남겨져있다.
print(TestClass.__dict__['stock_num'])

user1 = TestClass("asdf")
print(user1.stock_num)  # 인스턴스로 변수가 할당되어있지 않으면 클래스 변수를 참조해서 가져온다. 만약 클래스 변수에도 없으면 에러


# 클래스 변수는 약간 공동 변수라고 생각하면된다. 글로벌 변수처럼. 하나의 변수를 모든 인스턴스와 공유함.

# 상속 기본


def test_function(*asdf, **blabla):
    result = asdf
    chap = blabla
    a = [result, chap]
    return a

# 메소드 오버라이딩 - 부모 클래스의 메소드를 수정해서 다르게 바꾸는것

# 부모 클래스의 method call - super().method_name()

# Inheritance.info
# mro 상속 정보를 list타입으로 알 수 있는 것

# Class.mro() 모든 상속의 정보를 알 수 있는 함수

# 모든 클래스는 object를 상속 받지만 기재하지 않아도 된다. 하지만 명시적으로 기재를 해도 상관없다.


