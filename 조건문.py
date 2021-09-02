# 코드업 조건문 문제 풀이

# 1166
# year = 2012

# if year % 4 == 0 and year % 100 != 0:
#     print('yes')

# elif year % 400 == 0:
#     print('yes')

# else:
#     print('no')


# 1167
# 조건문 대신 sort() 정렬 메소드를 쓰는게 편리하다
# a = int(20)
# b = int(20)
# c = int(3)

# list = [a, b, c]
# list.sort()

# print(list[1])


# 1168
# m = '080521'
# s = 1

# if s == 1 or s == 2:
#     result1 = int(m)//10000
#     result2 = 100 - result1 + 12 + 1
#     print(result2)

# else:
#     result1 = int(m)//10000
#     result2 = 12 - result1 + 1
#     print(result2)


# 1169
# 나이 구하는 방법
# age = '105'
# year = 2012 - int(age) + 1


# if year < 2000:
#     result = ''.join(list(reversed(str(year))))

#     age = int(result)//100
#     result = ''.join(list(reversed(str(age))))
#     n = int(1)
#     print(int(result), n)

# else:
#     result = ''.join(list(reversed(str(year))))

#     age = int(result)//100
#     result = ''.join(list(reversed(str(age))))
#     n = int(3)
#     print(int(result), n)


# 1170
# 학번 구하는 방법
# grade = 3
# room = 1
# number = 2

# print(grade, room, number)

# if number < 10:
#     print(str(grade)+str(room)+str(0)+str(number))

# else:
#     print(str(grade)+str(room)+str(number))
