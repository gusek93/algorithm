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
# card = [10, 3, 4, 1, 10, 2, 6, 7, 5, 9]
# cardlist = []
# miss = []

# for i in range(1, card+1):
#     cardlist.append(i)


# for i in range(0, card-1):
#     num = int(card)
#     miss.append(i)


# for n in miss:
#     cardlist.remove(n)

# print(cardlist[0])


# 1412
# 노가다 성으로 풀수 있지만 for 문을 이용해서 풀어본다.
# n = 'oh! my god!'

# for i in n:
#     resulta = i.count('a')
#     resultb = i.count('b')
#     resultc = i.count('c')
#     resultd = i.count('d')
#     resulte = i.count('e')
#     # print(i.count('b'))
#     # print(i.count('c'))
#     # print(i.count('d'))
#     # print(i.count('e'))
#     # print(i.count('f'))
#     # print(i.count('g'))
#     # print(i.count('h'))
#     # print(i.count('i'))

# print('a:'+str(resulta))
# print('b:'+str(resultb))
# print(resultc)
# print(resultd)
# print(resulte)


# str = 'oh! my god!'
# li = [0 for _ in range(26)]

# for i in str:
#     if i >= 'a' and i <= 'z':
#         li[ord(i)-97] += 1

# for i in range(26):
#     print("%c:%d" % (chr(i+97), li[i]))


# 1416
# n = 7
# print(int(bin(n)[2:]))


# 1420
# n = int(5)
# hash_record = {}

# for i in range(5):
#     name, score = 'minsu 78'.split()
#     hash_record[name] = int(score)

# data = sorted(hash_record.items(), lambda t: t[1], reverse=True)
# print(data[2][0])


# 1425
# 표현 에러라는데 에러는 코드 문제는 아닌거 같은데..
# n = int(9)
# h = int(6)
# count = 0

# numlist = [160, 165, 164, 165, 150, 165, 168, 145, 170]
# numlist.sort()
# for i in numlist:
#     count += 1
#     print(i, end=' ')
#     if count == h:
#         print()
