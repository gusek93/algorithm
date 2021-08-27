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
n = int(4)

while n >= 0 and n <= 100:
    n += n
    print(n)
