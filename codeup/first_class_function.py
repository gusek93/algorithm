def square(x):
    return x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i)) # square 함수 호출, func == square
    return result

num_list = [1, 2, 3, 4, 5]

squares = my_map(square, num_list)

print(squares)


# def square(x):
#     return x * x
# num_list = [1, 2, 3, 4, 5]

# @square
# def my_map(num_list):
#     result = []
#     for i in num_list:
#         result.append(i) # square 함수 호출, func == square
#     return result



# squares = my_map()

# print(squares)

# def logger(msg):
#     def log_message():  # 1
#         print('Log: ', msg)

#     return log_message


# log_hi = logger('Hi')
# print(log_hi)  # log_message 오브젝트가 출력됩니다.
# log_hi()  # "Log: Hi"가 출력됩니다.

# del logger  # 글로벌 네임스페이스에서 logger 오브젝트를 지웁니다.

# # logger 오브젝트가 지워진 것을 확인합니다.
# try:
#     print(logger)
# except NameError:
#     print('NameError: logger는 존재하지 않습니다.')

# log_hi()  # logger가 지워진 뒤에도 Log: Hi"가 출력됩니다.