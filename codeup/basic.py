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

# n = input()
# number = map(int, input().split())

# numberlist = []

# for i in number:
#     numberlist.append(i)

# numberlist.sort()
# print(numberlist[-1])


# jonbob = map(int, input().split())
# sumlist = []

# for i in jonbob:
#     if i % 2 == 0:
#         result1 = (i//2)*10
#         sumlist.append(result1)

#     elif i % 2 != 0:
#         result2 = (i//2)+1
#         sumlist.append(result2)

# sum = 0
# for j in sumlist:
#     sum += j

# print(sum)

# n = int(input())

# for i in range(1,n+1):
#     if n % i == 0:
#         print(i, end=' ')

# n = int(input())
# result = 0

# for i in range(2,n):
#     if n % i == 0 :
#         result = 1

# if result == 0 :
#     print('prime')

# else:
#     print('not prime')


# n,k = map(int, input().split())

# result = n**k

# print(result)

# n = int(input())
# result = 1

# for i in range(1,n+1):
#     result *= i

# print(result)
