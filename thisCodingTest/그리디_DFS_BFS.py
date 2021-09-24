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


# 4-2 시각
# 3이 포함되는 경우의 수 출력 하기 // 완전 탐색 알고리즘 유형
# h = int(5)
# count = 0

# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1

# print(count)


# 왕실 나이트 실전 문제
# input_data = 'h3'
# # 시작 위치 찾기
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1

# # 나이트 이동 방향 정의
# steps = [(2, -1), (2, 1), (-2, -1), (-2, 1),
#          (1, -2), (-1, -2), (1, 2), (1, -2)]

# result = 0
# for step in steps:
#     # 이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]

#     # 해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result += 1

# print(result)


# 게임 개발 실전 문제
# n, m = map(int, input().split())

# # 방문 위치를 저장 하기 위해 맵을 생성 하여 0으로 초괴화(컴프리 헨션)
# d = [[0]*m for _ in range(n)]
# # 현재 캐릭터의 x좌표, y좌표 방향을 입력 받는다.
# x, y, direction = map(int, input().split())
# d[x][y] = 1  # 현재 좌표 방문 처리

# # 전체 맵 정보를 입력 받기
# array = []
# for i in range():
#     array.append(list(map(int, input().split())))

# # 북, 동, 남, 서 방향 정의 / 동서남북 이동할수 있는 좌표 / 예시 (-1,0), (0,1) . . .
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# # 왼쪽으로 회전


# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3


# # 시뮬레이션 시작
# count = 1
# turn_time = 0
# while True:
#     # 왼쪽으로 회전
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     # 회전 이후 정면에 가보지 않은 칸이 존재 하는 경우 이동
#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] = 1
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue

#     # 회전 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
#     else:
#         turn_time += 1

#     # 네 방향 모두 갑수 없는 경우
#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         # 뒤로 갈수 있다면 이동하기
#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
#         # 뒤가 바다로 막혀있을 경우
#         else:
#             break
#         turn_time = 0

# print(count)


# 5-5 팩토리열 2가지 방식으로 구현 하는 방법
# 반복적으로 구현 하기
# def factorial_iterative(n):
#     result = 1
#     # 1부터 n 까지의 수를 차례대로 곱하기
#     for i in range(1, n + 1):
#         result *= i

#     return result


# print(factorial_iterative(5))

# # 재귀적으로 구현 하기


# def factorial_recursive(n):
#     if n <= 1:
#         return 1
#     # n! = n * (n-1)! 를 그대로 코드에 작성
#     return n * factorial_recursive(n - 1)


# print(factorial_recursive(5))


# DFS 예제 (깊이 우선)
# DFS 메서드 정의
# def dfs(graph, v, visited):
#     # 현재 노드를 방문 처리
#     visited[v] = True
#     print(graph)
#     #print(v, end=' ')
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)


# # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]
# # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
# visited = [False] * 9

# # 정의된 DFS 함수 호출
# dfs(graph, 1, visited)


# BFS 예저 (너비 우선)
# from collections import deque

# # BFS 메서드 정의


# def bfs(graph, start, visited):
#     # 큐 구현을 위해 deque 라이브러리 사용
#     queue = deque([start])
#     # 현재 노드를 방문 처리
#     visited[start] = True
#     # 큐가 빌 떄까지 반복
#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')

#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True


# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# visited = [False] * 9
# bfs(graph, 1, visited)


# 실전 문제 음료수 얼려먹기
# n, m = map(int, input().split())

# # 2차원 리스트의 맵 정보 입력 받기
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))


# # DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
# def dfs(x, y):
#     # 주어진 범위를 벗어나는 경우에는 즉시 종료 (n x m 틀을 벗어 날 수 없다.)
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False

#     # 현재 노드를 방문 하지 않았다면
#     if graph[x][y] == 0:
#         # 해당 노드 방문 처리
#         graph[x][y] = 1
#         # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False


# # 모든 노드(위치)에 대하여 음료수 채우기
# result = 0
# for i in range(n):
#     for j in range(m):
#         # 현재 위치에서 DFS 수행
#         if dfs(i, j) == True:
#             result += 1

# print(result)


# 미로 탈출 예제
# from collections import deque

# # n,m을 공백으로 구분하여 받기
# n, m = map(int, input().split())

# # 2차원 배열 정보 받기
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))

# # 이동 방향 정의
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # BFS 소스 구현 코드


# def bfs(x, y):
#     # 큐 구현을 위해 deque 라이브러리 사용
#     queue = deque()
#     queue.append((x, y))

#     # 큐가 빌 때까지 반복
#     while queue:
#         x, y = queue.popleft()
#         # 현재 위치에서 네 방향으로 위치 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#         # 미로 공간에서 벗어난 경우 무시
#         if nx < 0 or ny < 0 or nx >= n or ny >= m:
#             continue
#         # 벽인 경우 무시
#         if graph[nx][ny] == 0:
#             continue
#         # 해당 노드를 처음 방문 하는 경우에만 최단 거리 기록
#         if graph[nx][ny] == 1:
#             graph[nx][ny] = graph[x][y] + 1

#     # 가장 오른쪽 아래까지의 최단거리 반환
#     return graph[n-1][m-1]


# print(bfs(0, 0))


a, b = input().split()

print(a)
