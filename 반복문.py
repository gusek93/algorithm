# 반복문 기초 연습문제 풀이


# 1251
# n = 1
# for i in range(n, 101):
#     print(i, end=' ')


# 1252
# n = int(5)
# for i in range(1, n + 1):
#     print(i, end=' ')


# 1253
# a = int(-1)
# b = int(1)

# list = [a,b]
# list.sort()

# a = list[0]
# b = list[1]

# for i in range(a, b+1):
#     print(i, end=' ')


# 1254
# 아스키코드 이용해서 풀기
# #ord(),chr()
# a = ord('b')
# b = ord('g')

# for i in range(a, b+1):
#     print(chr(i), end=' ')


# 1255
# float 으로 문제를 풀수 없음
# a = -2.00
# b = -1.00

# a = int(a * 100)
# b = int(b * 100)

# if 0 < a < b:
#     for i in range(a, b + 2):

#         print('%.2f' % (i*0.01), end=' ')

# elif a == b:
#     for i in range(a, b+1):

#         print('%.2f' % (i*0.01), end=' ')

# else:
#     for i in range(a - 1, b+1):

#         print('%.2f' % (i*0.01), end=' ')


# 1256
# 숫자 문자로 치환 replace()
# n = 5

# for i in range(0, n):
#     print(str(i).replace(str(i), "*"), end='')


# 1257
# a = int(2)
# b = int(7)

# for i in range(a, b + 1):
#     if i % 2 != 0:
#         print(i, end=' ')


# 1258
# n = int(100)
# total = 0
# for i in range(0, n + 1):
#     total = total + i

# print(total)


# 1259
# n = int(5)
# total = int(0)

# for i in range(0, n + 1):
#     if i % 2 == 0:
#         total += i

# print(total)


# 1260
# a = int(999)
# b = int(999)
# total = int(0)

# for i in range(a, b+1):
#     if i % 3 == 0:
#         total += i

# print(total)


# 1261
# n = map(int, input().split())
# n = list(n)
# b=0
# for i in n:
#     if i%5==0:
#         print(i)
#         break
#     else:
#         b+=1
# if b==len(n):
#     print(0)


# 1265
# n = int(2)
# i = int(0)

# while i < 9:
#     i += 1
#     print(str(n)+'*'+str(i)+'='+str(n*i))


# 1266
#n = int(input())
#numbers = list(map(int, input().split()))
# numbers = [3, 5, 7, 7, 2]
# total = int(0)

# for i in numbers:
#     total += i

# print(total)


# 1267
# n = int(5)
# numbers = [3, 5, 7, 15, 2]
# total = 0

# for i in numbers:
#     if i % 5 == 0:
#         total += i

# print(total)


# 1268
# n = int(5)
# numbers = [3, 5, 7, 15, 2]
# total = 0

# for i in numbers:
#     if i % 2 == 0:
#         total += 1

# print(total)


# 1269
a = 2
b = -1
c = 3
n = 5
result = a * b + c

while 1 <= n <= 9:
    n += 1
    for i in result:
        result = i * b * c

print(result)
