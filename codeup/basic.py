# 기초를 다지자
# for i in range(1,100+1):
#     print(i,end=' ')

# n = int(input())

# for i in range(1,n+1):
#     print(i,end=' ')


# a,b = map(int, input().split())

# if a > 0 and b > 0 :
#     for i in range(a,b+1):
#         print(i, end=' ')

# elif a > b:
#     for i in range(b, a+1):
#         print(i, end=' ')


# else:
#     for i in range(a, b+1):
#         print(i, end=' ')


# start,end = input().split()

# a = ord(start)
# b = ord(end)

# for i in range(a,b+1):
#     print(chr(i), end=' ')


# n = int(input())

# for i in range(1,n+1):
#     if i == n:
#         print('*'*i)


# a,b = map(int, input().split())

# for i in range(a, b+1):
#     if i % 2 != 0:
#         print(i ,end=' ')

# a,b = map(int, input().split())
# total = 0

# for i in range(a,b+1):
#     if i % 3 == 0 :
#         total += i

# print(total)

# number = input().split()

# numberList = number
# b=0
# for i in numberList:
#     if int(i) % 5 == 0:
#         print(int(i))
#         break

#     else:
#         b += 1

# if b == len(numberList):
#     print(0)


# n = int(input())

# for i in range(1,9+1):
#     num = n*i
#     print(f'{n}*{i}={num}')


# a = input()
# b = input().split()

# numberList = b
# total = 0

# for i in numberList:
#     if int(i) % 2 == 0:
#         total += 1

# print(total)


# a,b,c,n = map(int, input().split())
# result = a

# for i in range(2,n+1):
#     result = result*b+c
# print(result)


# n = int(input())
# count = 0

# for i in range(1,n+1):
#     if i % 10 ==1:
#         count += 1

# print(count)

n = input()
number = map(int, input().split())

numberlist = []

for i in number:
    numberlist.append(i)

numberlist.sort()
print(numberlist[-1])

