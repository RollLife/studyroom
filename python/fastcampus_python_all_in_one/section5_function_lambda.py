# *args, *kwargs


# 가변인자, 몇개의 인자가 넘어갈지 모르는 인자 , 다양한인자를 넘겼을대 튜플형태로 넘어감
def args_func(*args):
    print(args)


args_func("kim", "Park", "lee")


# kwargs => 키워드 인자

# dictionary 형태의 가변인자, 여러개의 인자를 넣을 수 있는것
def kwagrs_func(**kwargs):
    print(kwargs)


kwagrs_func(name="kim")


def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


# 가변인자는 없어도 된다. 필수가 아니기때문
example_mul(10, 20)

# 효율적인 함수 호출을 할 수 있다.
example_mul(10, 'park', 'kim', age=1)


# 중첩함수(클로저) ** 필수
def nested_func(num):
    def func_in_func(num):
        print(num)

    print("in func")
    func_in_func(num + 1000)


nested_func(10000)


# type hint
def func_mul3(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300

    return [y1, y2, y3]


print(func_mul3(5))


# 람다식
# 메모리절약, 가독성 향상, 코드 간결 등..
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num: int) -> int:
    return num * 10


var_func = mul_10
print(var_func)  # 일반적 객체를 생성해서 메모리에 올려놓음

# 람다 함수
# 메모리 절약, 하지만 가독성에는 많이 좋지 않을 수 있으
lambda_mul_10 = lambda num: num * 10
print(lambda_mul_10(100))


def func_final(x, y, func):
    print(x * y * func(10))


# 람다 함수 호출
func_final(10, 10, lambda_mul_10)

# 즉시 람다 함수 호출하여 인자로 넘겨줌
print(func_final(10, 10, lambda x: x * 1000))
