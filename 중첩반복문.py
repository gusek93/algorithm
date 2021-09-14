# 코드업 충첩 반복문 기초 문제 풀이

# 1351
# first = int(5)
# last = int(9)

# for i in range(first, last + 1):
#     for j in range(1, 9 + 1):
#         print(str(i)+'*'+str(j)+'='+str(i * j))


# 1352
# n = int(4)

# for i in range(1, n+1):
#     print('*'*n)


# 1353
# n = int(3)
# result = 0

# for i in range(1, n+1):
#     result = i
#     print('*'*result)


# 1354
# n = int(3)

# for i in range(n, 0, -1):
#     print('*' * i)


# 1355
# n = int(3)

# for i in range(0, n):
#     for j in range(0, i):
#         print(' ', end='')
#     for j in range(0, n-i):
#         print('*', end='')

#     print()


# 1356
# n = int(15)

# for i in range(0, n):
#     if i == 0 or i == n-1:
#         for j in range(0, n):
#             print('*', end='')
#         print()

#     else:
#         print('*', end='')
#         for j in range(0, n-2):
#             print(' ', end='')
#         print('*', end='')
#         print()


# 1357
# n = int(7)

# for i in range(1, n+1):
#     print('*' * i)

# for j in range(n-1, 0, -1):
#     print('*' * j)


# 1358
# n = int(5)

# for i in range(1, n + 1):
#     if i % 2 != 0:
#         a = '*'*i
#         print(a.center(n))


# 1361
# n = int(3)

# for i in range(0, n):
#     print(' ' * i, end='')
#     print('**', end='')
#     print()


# 1365
# 잘 이해 못하겠다.. if 조건을 자세히 보자
# n = int(9)

# for i in range(0, n):
#     print('*', end='')
# print()

# for i in range(1, n-1):
#     for j in range(0, n):
#         if((j == 0) or (j == i) or (j == n-1) or (j == n-i-1)):
#             print('*', end='')
#         else:
#             print(' ', end='')

#     print()

# for i in range(0, n):
#     print('*', end='')
# print()


# 1366

# n = int(17)
# for i in range(0, n):
#     print('*', end='')
# print()

# for i in range(1, n-1):
#     for j in range(0, n):
#         if((j == 0) or (j == i) or (j == n-1) or (j == n-i-1) or (n-1)/2 == j or (n-1)/2 == i):
#             print('*', end='')
#         else:
#             print(' ', end='')

#     print()

# for i in range(0, n):
#     print('*', end='')
# print()


# 1367
# n = int(4)

# for i in range(n-1, 0, -1):
#     print(' ' * i, end='')
#     print('*' * n, end='')
#     print()

# print('*'*n)


# 1368
# h = int(5)
# k = int(4)
# d = 'R'

# if d == 'L':
#     for i in range(0, h):
#         print(' '*i, end='')
#         print('*' * k, end='')
#         print()

# else:
#     for i in range(h-1, 0, -1):
#         print(' ' * i, end='')
#         print('*' * k, end='')
#         print()
#     print('*'*k)

# 중첩반복으로 풀이
# h = int(5)
# k = int(4)
# d = 'R'

# if d == 'L':
#     for i in range(0, h):
#         for j in range(0, i):
#             print(' ', end='')
#         for j in range(0, k):
#             print('*', end='')
#         print()

# else:
#     for i in range(h-1, -1, -1):
#         for j in range(0, i):
#             print(' ', end='')
#         for j in range(0, k):
#             print('*', end='')
#         print()


# 1369
