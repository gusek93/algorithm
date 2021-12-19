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

# n = int(input())
# nlist = input().split()

# numberList = nlist

# #print(numberList[0],numberList[n//2],numberList[n-1])

# for i in range(0,n):
#     if i == 0:
#         print(numberList[i], end=' ')
#     elif n // 2 == i:
#         print(numberList[i//2], end=' ')
#     elif n-1 == i:
#         print(numberList[n-1], end=' ')


# n = input()

# print(len(n))


# a,b = map(int, input().split())

# result1 = 0
# result2 = 0

# for i in range(a,b+1):
#     if i % 2 == 0:
#         result1 -= i
#     elif i % 2 != 0:
#         result2 += i

# print(result2+result1)


# a,b = map(int,input().split())
# addNumber = 0
# subtractionNumber = 0
# numberList = []


# for i in range(a,b+1):
#     if i % 2 != 0:
#         addNumber += i

#     elif i % 2 == 0:
#         subtractionNumber -= i

# for j in range(a,b+1):
#     if j % 2 != 0:
#         numberList.append(f'+{j}')
    
#     elif j % 2 == 0:
#         numberList.append(f'-{j}')


# for i in numberList:
#     if numberList[0] == i :
#         print(int(i), end='')
#     else:
#         print(i,end='')

# print(f'={addNumber+subtractionNumber}')

#import math

# n = int(input())

# #squareRoot = math.floor(math.sqrt(n))
# #print(squareRoot)

# for i in range(1,n+1):
#     # if math.sqrt(i) == squareRoot:
#     #     result = n-i
#     if i*i <= n:
#         result = i


# print(n-result*result, result)


# money = int(input())
# date = int(input())
# persent = map(int, input().split())
# money = int(10000)
# date = int(1)
# persent = [10,-10,5,-5]

# originMoney = money


# for i in persent:
#     money += money*i/100

# #print(money)


# if money > originMoney:
#     print(round(money-originMoney))
#     print('good')

# elif money < originMoney:
#     print(round(money-originMoney))
#     print('bad')

# elif money == originMoney:
#     print(round(money-originMoney))
    # print('same')

# n = int(input())

# measureList = []

# for i in range(1,n+1):
#     if n % i == 0:
#         measureList.append(i)

# if len(measureList) == 4 and n % 2 != 0:
#     print(measureList[1],measureList[2])

# elif n == 6:
#     print(measureList[1], measureList[2])

# else:
#     print('wrong number')



# n = '3+3-3*3/3='
# numberList = []
# count = 0
# sum = 0
# minus = 0
# multiply = 0
# divide = 0
# result = 0

# for i in n:
#     numberList.append(i)

# for j in numberList:
#     if j == '+':
#         result += result+int(numberList[count-1])
 
    
#     elif j == '-':
#         result += result-int(numberList[count-1])
     
    # elif j == '*':
    #     multiply *= int(numberList[count-1])
    #     result
    #     print(multiply)

    # elif j == '/':
    #     divide /= int(numberList[count-1])
    #     print(divide)

#     elif j == '=':
#         break

#     count += 1


# print(result)


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())

# numberList = [a,b,c,d,e]

# numberList.sort()

# print(numberList[-1])
# print(numberList[0])


# n = int(input())

# for i in range(1,9+1):
#     print('*'*n*i)


# string = input()

# #transrate = ord(string)

# #print(ord(string))


# for i in string:
#     if 96 < ord(i)+23 < 123 :
#         print(chr(ord(i)+23),end='')
    
#     elif ord(i)+23 > 122:
#         print(chr(ord(i)+23-122+97-1), end='')
    
#     elif ord(i) == 32:
#         print(chr(ord(i)),end='')



# string = input()

# for i in string:
#     if 96 < ord(i)-23 < 123:
#         print(chr(ord(i)-23), end='')

#     elif 32 < ord(i)-23 < 97:
#         print(chr(ord(i)-23+26), end='')

#     elif ord(i) == 32:
#         print(chr(ord(i)), end='')

# string = input()

# for i in string:
#     if 64 < ord(i) < 91:
#         print(chr(ord(i)+32),end='')

#     elif 96 < ord(i) < 123:
#         print(chr(ord(i)-32),end='')

#     else:
#         print(i,end='')

# x,y = map(int, input().split())

# for i in range(x,y+1):
#     for j in range(1,9+1):
#         print(f'{i}*{j}={i*j}')


# n = int(input())
# reverse = []

# for i in range(1,n+1):
#     reverse.append(i)

# reverse.reverse()

# for j in reverse:
#     print('*'*j)


n = int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        print('*'*i*j)