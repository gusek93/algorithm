# 파이썬 알고리즘 연습장
# https://codeup.kr/problemsetsol.php?psid=33
# 코딩테스트 파이썬 기초 100제 문제 풀이 기록(파이써은 6000번 부터 )


# 6059
# 비트 연산자로 출력
# a = int(2)
# print(~a)


# 6060
# 비트 연산자 비교
# a = int(3)
# b = int(5)
# c = a & b
# print(c)


# 6061
# a = int(3)
# b = int(5)
# c = a | b
# print(c)


# 6062
# a = int(3)
# b = int(5)
# c = a ^ b
# print(c)


# 6063
# 3항 연산자
# a = int(123)
# b = int(456)
# c = (a if (a >= b) else b)
# print(c)


# 6064
# a = int(3)
# b = int(-1)
# c = int(5)
# d = (a if a < b else b) if ((a if a < b else b) < c) else c
# print(d)


# 6065
# 조건 선택 실행(짝수만 출력)
# a, b, c = input().split()

# a = int(a)
# b = int(b)
# c = int(c)

# if a % 2 == 0 :
#     print(a)

# if b % 2 == 0 :
#     print(b)

# if c % 2 == 0 :
#     print(c)


# 6066
# a,b,c = map(int, input().split())

# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")

# if b % 2 == 0:
#     print("even")
# else:
#     print("odd")

# if c % 2 == 0:
#     print("even")
# else:
#     print("odd")


# 6067
# n = int(-2147483648)

# if n < 0:
#     if n % 2 == 0:
#         print('A')
#     else:
#         print('B')

# else:
#     if n % 2 == 0:
#         print('C')
#     else:
#         print('D')


# 6068
# 점수별 등급 매기기
# n = int(input())

# if n >= 90 :
#     print('A')

# elif n >= 70 :
#     print('B')

# elif n >= 40 :
#     print('C')

# else :
#     print('D')


# 6069
# a = str('A')

# if a == 'A':
#     print('best!!!')

# elif a == 'B':
#     print('good!!')

# elif a == 'C':
#     print('run!')

# elif a == 'D':
#     print('slowly~')

# else:
#     print('what?')


# 6070
# m = int(input())

# if m//3 == 1 :
#     print("spring")

# elif m//3 == 2 :
#     print("summer")

# elif m//3 == 3 :
#     print("fall")

# else :
#     print("winter")


# 6071
# while 문
# n = 1

# while n != 0 :
#     n = int(input())
#     if n != 0 :
#         print(n)


# 6072
# n = int(input())

# while n != 0 :
#     print(n)
#     n = n - 1


# 6073
# n = int(input())

# while n != 0 :

#     n = n - 1
#     print(n)


# 6074
# c = ord(input())
# t = ord('a')
# while t<=c :
#   print(chr(t), end=' ')
#   t += 1

# 6075
# n = int(4)
# i = 0
# while i <= n:
#     print(i)
#     i += 1


# 6076
# n = int(4)
# for i in range(n+1):
#     print(i)


# 6077
# 짝수의 합 구하기
# n = int(5)
# s = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         s += i
# print(s)


# 6078
# while True:
#     x = input()
#     print(x)
#     if x == 'q':
#         break


# 6079
# n = int(1000)
# s = 0
# t = 0
# while s < n:
#     t = t+1
#     s = s+t
# print(t)


# 6080
# n, m = map(int, input().split())
# n = 2
# m = 3
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         print(i, j)


# 6081
# n = int('F', 16)
# for i in range(1, 16):
#     print('%X' % n, '*%X' % i, '=%X' % (n*i), sep='')


# 6082
# n = int(30)
# for i in range(1, n+1):
#     if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
#         print("X", end=' ')

#     else:
#         print(i, end=' ')


# 6083
# r, g, b = map(int, input().split())
# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             print(i, j, k)

# print(r*g*b)


# 6084
# h, b, c, s = map(int, input().split())

# m = (h * b * c * s)/8/1024/1024

# print('%.1f MB' % m)


# 6085
# w, h, b = map(int, input().split())

# m = (w * h * b)/8/1024/1024

# print('%.1f MB' % m)


# 6086
# n = int(57)
# c = 0
# s = 0
# while True:
#     s += c
#     c += 1
#     if s >= n:
#         break

# print(s)


# 6087
# n = int(10)

# for i in range(1, n+1):
#     if i % 3 == 0:
#         continue
#     print(i, end=' ')


# 6088
# a = int(1)
# d = int(3)
# n = int(5)

# for i in range(1, n):
#     a = a + d
#     print(a)


# 6089
# a = int(2)
# r = int(3)
# n = int(7)

# for i in range(1, n):
#     a *= r

# print(a)


# 6090
# a = int(1)
# m = int(-2)
# d = int(1)
# n = int(8)

# for i in range(1, n):
#     a = a * m + d
# print(a)


# 6091
# 최소 공배수 구하는 문제
# a = int(3)
# b = int(7)
# c = int(9)
# d = int(1)

# while d % a != 0 or d % b != 0 or d % c != 0:
#     d = d + 1

# print(d)


# 6092
# n= int(input())
# a=list(map(int,input().split()))
# d=[]
# for i in range(24):
#     d.append(0)
# for i in range(n):
#     d[a[i]]+=1
# for i in range(1,24):
#     print(d[i],end=' ')


# 6093
# n = int(input())
# a = input().split()

# for i in range(n):
#     a[i] = int(a[i])

# for i in range(n-1, -1, -1):
#     print(a[i], end=' ')


# 6094
# 리스트 최소값 출력
# n = int(input())
# k = map(int, input().split())
# a = min(k)

# print(a)


# 6095
# 2차원 배열 문제
# d = []
# for i in range(20):
#     d.append([])
#     for j in range(20):
#         d[i].append(0)

# n = int(input())
# for i in range(n) :
#     x, y = input().split()
#     d[int(x)][int(y)] = 1

# for i in range(1, 20):
#     for j in range(1,20):
#         print(d[i][j], end= ' ')
#     print()


# 6096
# a = [[]*19 for _ in range(19)]
# for i in range(19):
#    a[i]=list(map(int,input().split()))

# n = int(input())

# for i in range(n):
#     b,c=map(int,input().split())

#     for j in range(19):
#         if(a[b-1][j]==1):
#             a[b-1][j]=0
#         else: a[b-1][j]=1

#     for j in range(19):
#         if(a[j][c-1]==1):
#             a[j][c-1]=0
#         else: a[j][c-1]=1

# for i in range(19):
#     for j in range(19):
#         print(a[i][j],end=' ')
#     print()


# 6097
# h,w = map(int,input().split())
# n = int(input())

# board=[[0]*w for _ in range(h)]

# for i in range(n):
#     l,d,x,y = map(int,input().split())
#     if(d==0):
#         for j in range(l):
#             board[x-1][y-1+j]=1
#     else:
#         for j in range(l):
#             board[x-1+j][y-1]=1


# for i in range(h):
#     for j in range(w):
#         print(board[i][j],end=' ')
#     print()


# 6098
# board=[[]*10 for _ in range(10)]
# for i in range(10):
#     board[i]=list(map(int,input().split()))
# x=1
# y=1
# board[x][y]=9

# while True:
#     if(board[x][y]==2):
#         board[x][y]=9
#         break
#     if(board[x][y+1]!=1):
#         board[x][y]=9
#         y+=1
#     else:
#         if(board[x+1][y]!=1):
#             board[x][y]=9
#             x+=1
#         else:
#           board[x][y]=9
#           break

# for i in range(10):
#     for j in range(10):
#         print(board[i][j],end=' ')
#     print()
