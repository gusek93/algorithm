# n = 1260
# count = 0
# coin_types = [500, 100, 50, 10]

# for coin in coin_types:
#     count += n
#     n = n % coin

#     print(count)


# 2.큰 수의 법칙
# 내가 푼 방법
# input = '5 8 3'
# listinput = [2, 4, 5, 4, 6]

# n, m, k = input.split()
# n = int(n)
# m = int(m)
# k = int(k)

# count = 0
# sum = 0

# listinput.sort()

# for i in range(1, m+1):
#     count += 1
#     if i % k == 0:
#         sum += listinput[-2]

#     else:
#         sum += listinput[-1]

# print(sum)


# 단순하게 푸는 예시
# input = '5 8 3'
# listinput = '2 4 5 4 6'

# n, m, k = map(int, input.split())
# data = list(map(int, listinput.split()))
# data.sort()
# first = data[n-1]
# second = data[n-2]
# result = 0

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1

#     if m == 0:
#         break
#     result += second
#     m -= 1

# print(result)

# m = 8
# k = 3
# # 가장 큰 수가 더해지는 횟수
# result = int(m / (k+1) * k + m % (k+1))

# print(result)

# 수열을 파악 하여 문제 풀이 방법
# input = '5 8 3'
# listinput = '2 4 5 4 6'

# n, m, k = map(int, input.split())
# data = list(map(int, listinput.split()))
# data.sort()
# first = data[n-1]
# second = data[n-2]
# result = 0

# count = int(m/(k+1))*k
# count += m % (k+1)

# result = 0
# result += (count) * first
# result += (m - count) * second

# print(result)


# 3. 숫자 카드 게임
# min 함수 이용 하는 방법
# input = '3 3'
# input2 = '1 2 3'
# n, m = map(int, input.split())

# result = 0

# for i in range(n):
#     data = list(map(int, input2.split()))
#     min_value = min(data)
#     result = max(result, min_value)

# print(result)


# # 2중 반복문 구조를 이용하는 방법
# input = '3 3'
# input2 = '2 1 3'
# n, m = map(int, input.split())

# result = 0

# for i in range(n):
#     data = list(map(int, input2.split()))
#     min_value = 10001
#     for a in data:
#         min_value = min(min_value, a)

#     result = max(result, min_value)

# print(result)


# 4. 1이 될떄 까지 문제 풀이
# n = int(25)
# k = int(5)
# result = 0

# while n >= k:
#     while n % k != 0:
#         n -= 1
#         result += 1

#     n //= k
#     result += 1

# while n > 1:
#     n -= 1
#     result += 1

# print(result)


# 입력값의 범위가 10억 이상이여도 시간 초과가 안나는
# n = int(25)
# k = int(3)
# result = 0

# while True:
#     target = (n // k) * k
#     result += (n - target)
#     n = target

#     if n < k:
#         break
#     result += 1
#     n //= k

# result += (n-1)
# print(result)


# 예제 4-1 상하 좌우
# n = int(5)
# commendlist = 'R R R U D D'.split()
# array = [[0]*n for _ in range(n)]
# count = 0

# for i in commendlist:
#     if i == 'R':
#         i[][+1]
#     elif i == 'L':
#         i[+1][]
#     elif i == 'U':
#         i[-1][]
#     else:
#         i == 'D'
#         i[][-1]

# for i in range(0, n):
#     for j in range(0, n):
#         count += 1
#         i += 1
#         array[i][j] = count

# for i in range(0, n):
#     for j in range(0, n):
#         print(array[i][j], end=' ')
#     print()


# 답안 예시
# n = int(5)
# x, y = 1, 1
# plans = 'R R R U D D'.split()

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]

#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue

#     x, y = nx, ny

# print(x, y)
