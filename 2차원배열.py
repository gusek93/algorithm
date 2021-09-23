# 코드업 2차원 배열 문제집
# n = int(5)

# for i in range(1, n**2+1):
#     print(i, end=' ')
#     if i % n == 0:
#         print()


# 1502
# n = int(3)
# matrix = [[0]*n for i in range(n)]
# cnt = 0

# for i in range(0, n):
#     for j in range(0, n):
#         cnt += 1
#         matrix[i][j] = cnt


# for i in range(0, n):
#     for j in range(0, n):
#         print(matrix[j][i], end=' ')
#     print()


# 1503
# 2차원 배열 만들떄 마지막에 한번더 선언해 주는 이유는 뭘까? 초기화?
# n = int(3)
# matrix = [[0]*n for i in range(n)]
# cnt = 0

# for i in range(0, n):
#     if i % 2:
#         for j in range(n-1, -1, -1):
#             cnt += 1
#             matrix[i][j] = cnt

#     else:
#         for j in range(0, n):
#             cnt += 1
#             matrix[i][j] = cnt

# for i in range(0, n):
#     for j in range(0, n):
#         print(matrix[i][j], end=' ')
#     print()


#  1504
# n = int(3)
# matrix = [[0]*n for i in range(n)]
# cnt = 0

# for i in range(0, n):
#     if i % 2:
#         for j in range(n-1, -1, -1):
#             cnt += 1
#             matrix[j][i] = cnt

#     else:
#         for j in range(0, n):
#             cnt += 1
#             matrix[j][i] = cnt

# for i in range(0, n):
#     for j in range(0, n):
#         print(matrix[i][j], end=' ')
#     print()


# 1505
# n = int(3)
# matrix = [[0]*n for i in range(n)]
# cnt = 0

# for i in range(0, n):
#     if i % 2:
#         for j in range(n-1, -1, -1):
#             cnt += 1
#             matrix[i][j] = cnt

#     else:
#         for j in range(0, n):
#             cnt += 1
#             matrix[i][j] = cnt


# for i in range(0, n):
#     for j in range(0, n):
#         print(matrix[i][j], end=' ')
#     print()


# 1461
# n = int(4)
# matrix = [[0]*n for i in range(n)]
# cnt = 0

# for i in range(0, n):
#     for j in range(n-1, -1, -1):
#         cnt += 1
#         matrix[i][j] = cnt

# for i in range(0, n):
#     for j in range(0, n):
#         print(matrix[i][j], end=' ')
#     print()


# 1096
# matrix = [[0]*19 for _ in range(19)]
# cnt = 0

# for i in range(0, 19):
#     for j in range(0, 19):
#         matrix[i][j]

# for i in range(0, 19):
#     for j in range(0, 19):
#         print(matrix[i][j], end=' ')
#     print()
