# 거스름돈 문제
# N = int(input())

# if N >= 500:
#     a = int(N/500)
#     w = N%500

#     if w >= 100:
#         b = int(w/100)
#         x = w%100
        
#         if x >= 50:
#             c = int(x/50)
#             y = x%50

#             if y >= 10:
#                 d = int(y/10)

#     result = a+b+c+d

# print(result)


# 간단한 풀이 방법
N = int(1260)
count = 0

coin_types = [500,100,50,10]

for coin in coin_types:
    count += N//coin
    N %= coin

print(N)