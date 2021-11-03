#file IO


# writelines -> list -> 파일로 저장

list= [1,2,3,4]
a = open("blabla.txt", "w")
a.writelines(list)
a.close()


# print로파일 저장-> 권장 x

print("asdfas", file=a)