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
# n = int(input())
# numbers = list(map(int, input().split()))
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
# a = -3
# b = -8
# c = -2
# n = 1
# result = a
# result = a * b + c

# if n != 1:
#     for i in range(0, n - 2):
#         result = result * b + c
#     print(result)

# else:
#     print(a)


# 1270
# n = 35
# result = 0

# for i in range(1, n + 1):
#     if i % 10 == 1:
#         result += 1

# print(result)


# 1271
# n = 5
# list = [3, 1, 29, 31, 21]
# list.sort()
# list.reverse()
# max = list[0]
# print(max)


# 1272
# n = int(1)
# m = int(2)

# if n % 2 == 0:
#     result = n/2 * 10

# else:
#     result = (n + 1)/2

# if m % 2 == 0:
#     result2 = m/2*10

# else:
#     result2 = (m + 1)/2

# print(int(result) + int(result2))


# 1273
# n = 6

# for i in range(1, n + 1):
#     if n % i == 0:
#         result = i
#         print(result, end=' ')


# 1274
# for 결과값을 list[] 에 추가 / append(i)
# n = 7453
# list = []

# for i in range(1, n+1):
#     if n % i == 0:
#         list.append(i)

# if len(list) == 2:
#     print("prime")
# else:
#     print("not prime")


# 1275
# n = 3
# k = 3
# result = n ** k
# print(result)


# 1276
# n = 5
# result = 1

# for i in range(1, n + 1):
#     result *= i

# print(result)


# 1277
# n = 7
# list = [2, 4, 7, 3, 1, 2, 5]

# min = list[0]

# mid = (len(list) - 1)/2
# mid2 = int(mid)

# max = len(list)-1
# max1 = int(max)

# print(list[0], list[mid2], list[max1])


# 1278
# n = str(932)
# print(len(n))


# 1279
# a = 5
# b = 7
# list = []
# sum1 = 0
# sum2 = 0

# for i in range(a, b + 1):
#     list.append(i)

# for i in list:
#     if i % 2 == 0:
#         sum1 += -i

#     else:
#         sum2 += i


# print(sum1+sum2)


# 1280
# a = 5
# b = 7
# list = []
# list2 = []
# sum1 = 0
# sum2 = 0

# for i in range(a, b+1):
#     list.append(i)

# for i in list:
#     if i % 2 == 0:
#         sum1 += -i
#         list2.append('-'+str(i))
#         print('-'+str(i), end='')

#     else:
#         sum2 += i
#         list2.append('+'+str(i))
#         print('+'+str(i), end='')

# result = sum1 + sum2
# print('=' + str(result))


# 1281
# a = 5
# b = 7
# list = []
# list2 = []
# sum1 = 0
# sum2 = 0

# for i in range(a, b + 1):
#     list.append(i)

# for i in list:
#     if i % 2 == 0:
#         sum1 += -i
#         list2.append(i)
#         print('-'+str(i), end='')

#     elif a == i:
#         sum2 += i
#         list2.append(-i)
#         print(str(i), end='')

#     else:
#         sum2 += i
#         list2.append(-i)
#         print('+'+str(i), end='')

# result = sum1 + sum2
# print('=' + str(result))


# 1283
a = 10000
b = 4
list = [10, -10, 5, -5]
list2 = []
seed = a
sum = 0
abs = 0

for i in list:
    if i > 0:
        sum = seed + (seed * (i/100))
        print(sum)
    else:
        sum = seed - (seed*(-i/100))
        print(sum)

print(round())
