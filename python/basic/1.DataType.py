"""
본 로직은 나도코딩 자료형 파트를 따라서 작성함을 알립니다.
https://www.youtube.com/watch?v=kWiCuklohdY&t=64s
"""

# [숫자 자료형]
print(5)  # >> 5 | 정수
print(-10)  # >> -10 | 음수
print(3.14)  # >> 3.14 | 실수
print(1000)  # >> 1000 | 큰 숫자
print(5 + 3)  # >> 8 | 연산
print(2 * 8)  # >> 16 | 곱연산
print(3 * (3 + 1))  # >> 12 | 다소 복잡한(?) 연산

# [문자형 자료형]
print('풍선')  # >> 풍선 |  single quotation
print("풍선")  # >> 풍선 |  double quotation
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")  # >> ㅋㅋㅋㅋㅋㅋㅋㅋㅋ | continuous string
print("ㅋ" * 9)  # >> ㅋㅋㅋㅋㅋㅋㅋㅋㅋ | 위와 같은 결과(숫자와 문자열을 조합하면 연속된 자료형의 갯수를 나타낼 수 있음)

# [Boolean 자료형]

# 참 / 거짓
print(5 > 10)  # >> False
print(5 < 10)  # >> True
print(True)  # >> True
print(False)  # >> False
print(not True)  # >> False
print(not (5 > 10))  # >> True | 5 > 10 - False => not False == True

# [변수]
# 애완동물을 소개해 주세요~ (변수로 지정하기 이전)
print("우리집 강아지의 이름은 연탄이예요")  # >> 우리집 강아지의 이름은 연탄이예요
print("연탄이는 4살이며, 산책을 아주 좋아해요")  # >> 연탄이는 4살이며, 산책을 아주 좋아해요
print("연탄이는 어른일까요? True")  # >> 연탄이는 어른일까요? True

# 변수 - 값을 저장하는 공간(ex : 강아지의 이름을 저장하는 공간)

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

# 변수로 지정한 애완동물 소개
print("우리집 " + animal + "의 이름은 " + name + "예요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")  # age는 숫자형이기때문에 문자형으로 조합하기 위해선 문자열 형변환 必
print(name + "는 어른일까요? " + str(is_adult))  # Boolean 역시 문자열로 조합시 문자열 형변환 必

# 해당 문구와 동일하게 다른 애완동물 소개
animal = "고양이"
name = "멍청이"
age = 2
hobby = "잠자기"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")  # age는 숫자형이기때문에 문자형으로 조합하기 위해선 문자열 형변환 必
print(name + "는 어른일까요? " + str(is_adult))  # Boolean 역시 문자열로 조합시 문자열 형변환 必

# 필요한 변수들만 변경하기
name = "냐옹이"
hobby = "마구할퀴기"

print("우리집 " + animal + "의 이름은 " + name + "예요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")  # age는 숫자형이기때문에 문자형으로 조합하기 위해선 문자열 형변환 必
print(name + "는 어른일까요? " + str(is_adult))  # Boolean 역시 문자열로 조합시 문자열 형변환 必

# 문자열 조합시 +가 아닌 ,로 조합
## ,가 들어가게되면 문자열마다 띄어쓰기가 되어버리게 된다.
### ,가 들어가면 굳이 문자열이 아닌 자료형에 대해서 문자열로 형변환 할 필요가 없다.

print("우리집 ", animal, "의 이름은 ", name, "예요")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")  # 콤마로 구분하기에 굳이 age(숫자 자료형)을 형변환 필요 X
print(name, "는 어른일까요? ", is_adult)  # 콤마로 구분하기에 굳이 is_adult(Boolean 자료형)을 형변환 필요 X

# [주석]

# 문자 맨 앞에 이와같이 #으로 시작하는 문자열들은 실제로 작동하는 코드에 포함되지 않는 문자들이다.
# 주로 어떨때 많이 쓰이냐면 로직에 대해 설명하거나 같이 개발하는 개발자들 혹은 동료들에게 언질 및 내용을 알려주기 위해 많이 사용한다.

# 주석 사용하는 방법

# 1. 한 문장을 주석처리 할때는 맨 앞에 #을 붙이기
''' 2. 여러개의 문장을 
주석 처리 할때는 
single quotation(작은 따옴표) 혹은
double quotation(쌍 따옴표)로 묶기
'''
# 3. 쉽게 주석 처리하는 방법은 주석처리할 코드를 드래그 혹은 선택하고 Ctrl + /(슬래쉬) 로 설정함.
# 4. 주석을 해제하는 방법은 역시 # 혹은 ''', """ 문자를 삭제하거나 Ctrl + /(슬래쉬)로 주석을 해제한다.(Ctrl + /로 주석해제 할수있는건 #으로
# 되어있는 문자만 가능
