# def decorator_function(original_function): 
#     def wrapper_function(*args, **kwargs): 
#         print("실행 전입니다.")
#         original_function(*args, **kwargs)
#         print("실행 끝났습니다.") 

#     return wrapper_function 

# @decorator_function
# def display(msg):  
#     print(msg)  


# #decorated_display = decorator_function(display)  

# display("hi")



def display(**msg):
    for key, value in msg.items():
        if 'python' in msg.keys():
            print('성공')
            
        else:
            print("{0} is {1}".format(key,value))
 

display(name='JS')
display(python='good')


