# def outer_func(): # 1
#     message = 'Hi' # 3

#     def inner_func(): # 4
#         print(message) # 6 

#     return inner_func # 5

# outer_func() # 2

# my_func = outer_func()

# my_func()



# def outer_func():  # 1
#     message = 'Hi'  # 3

#     def inner_func():  # 4
#         print(message)  # 6

#     return inner_func  # 5

# my_func = outer_func()  # 2

# print(my_func)  # 7
# print()
# print(dir(my_func))  # 8
# print()
# print(type(my_func.__closure__))  # 9
# print()
# print(my_func.__closure__)  # 10
# print()
# print(my_func.__closure__[0])  # 11
# print()
# print(dir(my_func.__closure__[0]))  # 12
# print()
# print(my_func.__closure__[0].cell_contents)  # 13



def outer_func(tag):  # 1
    tag = tag  # 5

    def inner_func(txt):  # 6
        text = txt  # 8
        print('<{0}>{1}<{0}>'.format(tag, text))  # 9

    return inner_func  # 7

h1_func = outer_func('h1')  # 2
p_func = outer_func('p')  # 3

h1_func('h1 태그의 안입니다.')  # 4
p_func('p 태그의 안입니다.')  # 10