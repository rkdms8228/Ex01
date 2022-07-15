# 문자형
s = ''
str1 = 'hello world'
str2 = '안녕'

print(s, str1, str2)
print(type(s), type(str1), type(str2))
print(isinstance(str2, str))

print(2, 4, 6, sep=" ")

print("===================================")

s01 = "aaa"
s02 = "aaa"
print(id(s01))
print(id(s02))

s02 = "aaaa"
print(id(s01))
print(id(s02))

print("===================================")

str = """abcdef
ghijk
lmn"""      # 줄바꿈하면 출력할 때도 여백 생김(주의)
print(str)

print("===================================")

print('Hello\nworld\nI\'d Say "hello World" ')
print('Hello\nworld\nI\'d Say \"hello World\" ')
print("Hello\rWorld")
print("Hello\bWorld")
print("Hello\tWorld")
