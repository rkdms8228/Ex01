age = 33
str1 = "현재 온도는 %d 도 입니다." % 23
str2 = "오늘은 %s년 %d 월 %d 일 입니다." % ("2017", 5, 11)
area = 76.483

print(str1)
print(str2)
print("제나이는 %d 살 입니다." % age )
print("원의 넓이는 %d 입니다." % area )

print("제나이는 %10d 살 입니다." % age )
print("제나이는 %-10d 살 입니다." % age )
print("원의 넓이는 %7.1f 입니다." % area )
print("원의 넓이는 %-20.1f 입니다." % area )

print("===================================")

age =35
print("제나이는 {0}살 입니다.".format(43) )
print("제나이는 {0}살 입니다.".format("스무") )
print("제나이는 {0}살 입니다.".format(age) )
print("오늘은 {0}년 {1} 월 {2} 일 입니다.".format("2017", 5, 11))
print("오늘은 {year}년 {month} 월 {day} 일 입니다.".format(year="2017", month=5, day=11))

print("오늘은 {0:<10}년 {1:>10} 월 {2:^10} 일 입니다.".format("2017", 5, 11))
