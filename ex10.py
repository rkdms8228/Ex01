str1 = "FirstString"
str2 = "SecondString"

print(str1 + str2)      # print(str1 +10) ->  문자열 + 문자열만 가능
print(str1*3)
print(str1[2])
print(str1[-4])
print(str2[2:5])        # 이상 : 미만
print(str2[1:9:3])      # 이상 : 미만 : 증가
print(str2[:9])
print(str2[2:])
print(len(str2))

print(str2[:])
print(str2[-6:-2])

print(str2[::-1])

name = "토마토"
name2 = name[:-1]

if("토마토" == name[::-1]):
    print("aaa")