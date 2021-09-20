# 1093
# 기껏 풀엇더니 파이썬으로 제출 안되는 문제네 ㅡㅡ

# n = int(10)
# inputlist = list(map(int, input().split()))
# outputlist = []

# for i in inputlist:
#     #print(i, end=' ')
#     cnt = inputlist.count(i)
#     outputlist.append(cnt)


# while len(outputlist) <= 23:
#     outputlist.append(0)

# print(outputlist)


# 1402
# n = int(5)
# datalist = [1, 3, 5, 6, 8]
# datalist.reverse()

# for i in datalist:
#     print(i, end=' ')


# 1403
# k = int(3)
# datalist = [1, 2, 3]

# for i in range(2):
#     for j in datalist:
#         print(j)


# 1405
# n = int(5)
# numlist = [1, 2, 3, 4, 5]

# for i in range(n):
#     for j in range(n):
#         print(numlist[i + j - n], end=' ')
#     print()


# 1407
# slist = ['abC', 'Def', 'gh']

# for i in slist:
#     print(i, end='')


# 1409
# list(map(int,input().split()))
# numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = int(4)

# print(numlist[n-1])


# 1410

# string = '((())()(()))'
# open = 0
# close = 0

# for i in range(0, len(string)):
#     if string[i] == '(':
#         open += 1

#     elif string[i] == ')':
#         close += 1

# print(open, close)


# 1411
card = [10, 3, 4, 1, 10, 2, 6, 7, 5, 9]
cardlist = []
miss = []

for i in card:
    cardlist.append(i)

cardlist.sort()


for j in range(1, len(cardlist)+1):
    miss.append(j)


for i in miss:
    cardlist.remove(i)

print(cardlist[0])
