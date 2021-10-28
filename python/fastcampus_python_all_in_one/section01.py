"""
기본 문법을 다루는 파트

아는 부분을 제외하고 내가 새롭게 알게되었거나 필요한 부분만 기재한다.
"""

# print
print("T", "E", "S", "T", sep="")

print("Roll", "Life", sep="")
print("blabla", "@naver.com", sep="@")

print("예아", end="")
print("이것은 무엇이지")

print("{} {} ".format("ㅁㄴㅇㄹ", "ㅁㅇㄴㄹ"))
print("{0} {1}".format(123, 123))
print("{0: 5d} {1: 5.4f}".format(123, 123.123123))
print("{a: 5d} {b: 5.4f}".format(a = 123, b =123.123123))