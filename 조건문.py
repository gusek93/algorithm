# 코드업 조건문 문제 풀이

# 1166
# year = 2012

# if year % 4 == 0 and year % 100 != 0:
#     print('yes')

# elif year % 400 == 0:
#     print('yes')

# else:
#     print('no')


# 1167
# 조건문 대신 sort() 정렬 메소드를 쓰는게 편리하다
# a = int(20)
# b = int(20)
# c = int(3)

# list = [a, b, c]
# list.sort()

# print(list[1])


# 1168
# m = '080521'
# s = 1

# if s == 1 or s == 2:
#     result1 = int(m)//10000
#     result2 = 100 - result1 + 12 + 1
#     print(result2)

# else:
#     result1 = int(m)//10000
#     result2 = 12 - result1 + 1
#     print(result2)


# 1169
# 나이 구하는 방법
# age = '105'
# year = 2012 - int(age) + 1


# if year < 2000:
#     result = ''.join(list(reversed(str(year))))

#     age = int(result)//100
#     result = ''.join(list(reversed(str(age))))
#     n = int(1)
#     print(int(result), n)

# else:
#     result = ''.join(list(reversed(str(year))))

#     age = int(result)//100
#     result = ''.join(list(reversed(str(age))))
#     n = int(3)
#     print(int(result), n)


# 1170
# 학번 구하는 방법
# grade = 3
# room = 1
# number = 2

# print(grade, room, number)

# if number < 10:
#     print(str(grade)+str(room)+str(0)+str(number))

# else:
#     print(str(grade)+str(room)+str(number))


# 1171
# grade = 2
# room = 20
# number = 111

# if room < 10:
#     if number < 10:
#         result = str(grade)+str(0)+str(room)+str(0)+str(0)+str(number)
#         print(result)

#     elif number < 100:
#         result = str(grade)+str(0)+str(room)+str(0)+str(number)
#         print(result)

#     elif number < 1000:
#         result = str(grade)+str(0)+str(room)+str(number)
#         print(result)

# elif room < 100:
#     if number < 10:
#         result = str(grade)+str(room)+str(0)+str(0)+str(number)
#         print(result)

#     elif number < 100:
#         result = str(grade)+str(room)+str(0)+str(number)
#         print(result)

#     elif number < 1000:
#         result = str(grade)+str(room)+str(number)
#         print(result)

# 한줄로 가능 한것을 뻘짖했다..
# grade = 2
# room = 20
# number = 111

# print('%d%02d%03d' % (grade, room, number))


# 1172
# a = 9
# b = 1
# c = 8

# list = [a, b, c]
# list.sort()
# print(str(list[0])+' '+str(list[1])+' '+str(list[2]))


# 1173
# h = 1
# m = 1

# if 0 < h < 24 and m < 59:
#     if m < 30:
#         h = h - 1
#         m = m + 30

#     else:
#         m = m - 30

# else:
#     if m < 30:
#         h = 23
#         m = m + 30

#     else:
#         m = m - 30
# print(h, m)


# 1180
# n = 19

# result = ''.join(list(reversed(str(n))))
# result2 = int(result)*2

# if result2 > 100:
#     result2 = result2 - 100
#     print(result2)
#     if int(result2) <= 50:
#         print('GOOD')
#     else:
#         print('OH MY GOD')
# else:
#     print(result2)
#     if int(result2) <= 50:
#         print('GOOD')
#     else:
#         print('OH MY GOD')

# 난이도 갑자기 왜 쉬워짐..?
# 1201
# n = 5

# if n == 0:
#     print(0)

# elif n < 0:
#     print('음수')

# else:
#     print('양수')


# 1202
# n = 80

# if n >= 90:
#     print('A')

# elif n >= 80:
#     print('B')

# elif n >= 70:
#     print('C')

# elif n >= 60:
#     print('D')

# else:
#     print('F')


# 1203
# n = 15

# if n > 20:
#     print('비만')

# elif 10 < n <= 20:
#     print('과체중')

# else:
#     print('정상')


# 1204
# n = 11

# if n % 10 == 1 and n != 11:
#     print(str(n)+'st')

# elif n % 10 == 2 and n != 12:
#     print(str(n)+'nd')

# elif n % 10 == 3 and n != 13:
#     print(str(n)+'nd')

# else:
#     print(str(n)+'th')


# 1205
# 좀더 효율적인 비교 방법은 없을까??

# a = float(2)
# b = float(-1)

# p = a + b
# m1 = a - b
# m2 = b - a
# x = a * b
# j1 = a ** b
# j2 = b ** a

# if x <= p and j1 <= x and j2 <= p and m1 <= p and m2 <= p:
#     print('%.6f' % p)

# elif p <= x and j1 <= x and j2 <= x and m1 <= x and m2 <= x:
#     print('%.6f' % x)

# elif p <= j1 and x <= j1 and j2 <= j1 and m1 <= j1 and m2 <= j1:
#     print('%.6f' % j1)

# elif p <= j2 and x <= j2 and j1 <= j2 and m1 <= j2 and m2 <= j2:
#     print('%.6f' % j2)

# elif p <= m1 and x <= m1 and j1 <= m1 and j2 <= m1 and m2 <= m1:
#     print('%.6f' % m1)

# elif p <= m2 and x <= m2 and j1 <= m2 and j2 <= m2 and m1 <= m2:
#     print('%.6f' % m2)


# 1206
# a = int(5)
# b = int(10)


# if a % b == 0:
#     result = (a // b)
#     print(str(b)+'*'+str(result)+'='+str(a))

# elif b % a == 0:
#     result = (b // a)
#     print(str(a)+'*'+str(result)+'='+str(b))

# else:
#     print('none')


# 1207
# a = int(1)
# b = int(1)
# c = int(0)
# d = int(0)

# p = a + b + c + d

# if p == 1:
#     print('도')

# elif p == 2:
#     print('개')

# elif p == 3:
#     print('걸')

# elif p == 4:
#     print('윷')

# else:
#     print('모')


# 1210
# menu1 = int(400)
# menu2 = int(340)
# menu3 = int(170)
# menu4 = int(100)
# menu5 = int(70)

# select1 = int(1)
# select2 = int(2)

# if select1 == 1 and select2 == 1:
#     if menu1 + menu1 <= 500:
#         print('no angry')
#     else:
#         print('angry')

# elif select1 == 1 and select2 == 2 or select1 == 2 and select2 == 1:
#     if menu1 + menu2 <= 500:
#         print('no angry')
#     else:
#         print('angry')


# elif select1 == 1 and select2 == 3 or select1 == 3 and select2 == 1:
#     if menu1 + menu3 <= 500:
#         print('no angry')
#     else:
#         print('angry')

# elif select1 == 1 and select2 == 4 or select1 == 4 and select2 == 1:
#     if menu1 + menu4 <= 500:
#         print('no angry')
#     else:
#         print('angry')

# elif select1 == 1 and select2 == 5 or select1 == 5 and select2 == 1:
#     if menu1 + menu5 <= 500:
#         print('no angry')
#     else:
#         print('angry')

# elif select1 == 2 and select2 == 2:
#     if menu2 + menu3 <= 500:
#         print('no angry')
#     else:
#         print('angry')

# elif select1 == 2 and select2 == 3:
#     if menu2 + menu3 <= 500:
#         print('no angry')
#     else:
#         print('angry')

# elif select1 == 2 and select2 == 4:
#     if menu2 + menu4 <= 500:
#         print('no angry')
#     else:
#         print('angry')

# elif select1 == 2 and select2 == 5:
#     if menu2 + menu5 <= 500:
#         print('no angry')
#     else:
#         print('angry')

# elif select1 == 3 and select2 == 3:
#     if menu3 + menu3 <= 500:
#         print('no angry')
#     else:
#         print('angry')

# elif select1 == 3 and select2 == 4:
#     if menu3 + menu4 <= 500:
#         print('no angry')
#     else:
#         print('angry')

# elif select1 == 3 and select2 == 5:
#     if menu3 + menu5 <= 500:
#         print('no angry')
#     else:
#         print('angry')

# elif select1 == 4 and select2 == 5:
#     if menu4 + menu5 <= 500:
#         print('no angry')
#     else:
#         print('angry')

# else:
#     if menu5 + menu5 <= 500:
#         print('no angry')
#     else:
#         print('angry')


# 1212
# a = int(155)
# b = int(5)
# c = int(150)

# list = [a, b, c]
# list.sort()

# a = list[0]
# b = list[1]
# c = list[2]

# if int(c) < int(a) + int(b):
#     print('yes')

# else:
#     print('no')


# 1214
# year = int(400)
# month = int(2)

# # 윤달 조건
# if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#     if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#         print(31)

#     elif month == 2:
#         print(29)

#     else:
#         print(30)

# else:
#     if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#         print(31)

#     elif month == 2:
#         print(28)

#     else:
#         print(30)


# 1216
# a = int(30)
# b = int(100)
# c = int(70)

# if b - c > a:
#     print('advertise')

# elif b - c == a:
#     print('does not matter')

# else:
#     print('do not advertise')


# 1218
# a = int(20)
# b = int(20)
# c = int(111)

# list = [a, b, c]
# list.sort()

# a = list[0]
# b = list[1]
# c = list[2]

# if a == b == c:
#     print('정삼각형')

# elif a + b > c and a == b or a + b > c and b == c:
#     print('이등변삼각형')

# elif a**2 + b**2 == c**2:
#     print('직각삼각형')

# elif a + b > c:
#     print('삼각형')

# else:
#     print('삼각형아님')


# 1222
# time = int(80)
# a = int(6)
# b = int(7)

# while time < 90:
#     time = time + 5
#     a = a + 1

# if a > b:
#     print('win')

# elif a == b:
#     print('same')

# else:
#     print('lose')
