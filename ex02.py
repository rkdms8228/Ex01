# 대입문
a = 1
b = a + 1

print(a)
print(b)
print(a + b)
print(a, b)

# 대입문 오류
# 1 + 3 = a

# 한 줄로 쓸 때 세미클론으로 구분
e = 3.5; f = 5.3
print(e, f)

# 여러 변수를 한번에 대입
g, h = 3.5, 5.3
print(g, h)

# 여러 개를 같은 값 10으로 대입
x = y = z = 10
print(x, y, z)

# 값 교환하기
e = 3.5
f = 5.3
e, f = f, e
print(e, f)

# 오류
#a = (b = c + d)

# 변수에 새로운 값을 할당하면 기존의 값을 잃어버리고 새로운 값으로 치환한다.
var01 = 1
print(var01)

var01 = "hello"
print(var01)
print(type(var01))