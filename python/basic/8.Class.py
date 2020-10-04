"""
본 로직은 나도코딩 클래스 파트를 따라서 작성함을 알립니다.
https://www.youtube.com/watch?v=kWiCuklohdY
"""

# Class (클래스)
# 스타크래프트

# 마린 : 공격 유닛, 군인. 총을 쓸 수 있으
name = "마린"  # 유닛의 이름
hp = 40  # 유닛의 체력
damage = 5  # 유닛의 공격력

print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {}, 공격력 {} \n".format(hp, damage))

# 탴크 : 공격 유닛, 탱크, 포를 쓸 수 있는데, 일반 모드 / 시즈 모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {}, 공격력 {} \n".format(tank_hp, tank_damage))


def attack(name, loccation, damage):
    """
    유닛이 공격하는 method
    :param name: 유닛 이름
    :param loccation: 공격 위치
    :param damage: 공격할 때 데미지
    :return:
    """
    print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}]".format(name, loccation, damage))


attack(name, "1시", damage)  # 마린이 공격
attack(tank_name, "1시", tank_damage)  # 탱크가 공격

# 여기서 탱크가 하나 더 생긴다면?

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("\n{} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {}, 공격력 {} \n".format(tank2_hp, tank2_damage))

attack(tank2_name, "1시", tank2_damage)


# 여기서 문제가 생긴다. 게임을 실제로 할때 유닛은 수없이 생기는데 이렇게 일일이 하나씩 만들어야 할까?
# >> 그래서 class가 필요함 (흔히 class를 붕어빵 틀이라고 말한다. 붕어빵은 하나인데 여러개 찍어내는것처럼 말이다.)

class Unit:
    def __init__(self, name, hp, damage):
        # 필요한 값들을 정의
        # init 함수
        # 파이썬에서 생성되는 생성자
        # init 함수에서 생성된 인자만큼 동일한 갯수의 인자들을 던져줘야함
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5)  # self를 제외한 나머지 인자에 값 전달
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
# tank = Unit("tank") # 정의된 argument만큼 전달하지 못하기때문에 오류가 발생됨
# marine과 tank는 Unit 클래스의 인스턴스라고 표현함

# >> 똑같은 클래스에서 서로 다른 유닛들을 생성하였음


# init 함수
# 파이썬에서 생성되는 생성자
# init 함수에서 생성된 인자만큼 동일한 갯수의 인자들을 던져줘야함
# marine과 tank는 Unit 클래스의 인스턴스라고 표현함


# 멤버변수
# 클래스 내에서 정의된 변수
# self.name, self.hp 같은 애들이 멤버변수

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {}, 공격력 : {}".format(wraith1.name, wraith1.damage))  # 멤버 변수를 외부에서 사용함.

# 레이스가 클로킹함
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True # 외부에서 clocking이라는 변수를 추가로 할당함

if wraith2.clocking == True:
    print("{}는 현재 클로킹 상태입니다.".format(wraith2.name))

# if wraith1.clocking == True: # Error!
#     print("{}는 현재 클로킹 상태입니다.".format(wraith2.name))

# >> wraith2에만 확장적으로 clocking이라는 멤버 변수가 추가가 되었지만 wraith1에는 clocking이라는 변수가 없음
#TIP) 어떤 객체에 대해서 확장적으로 변수를 할당할 수 있고, 할당한 객체만 적용이되고 다른 객체에는 적용이 되지않는다.


