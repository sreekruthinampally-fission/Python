#1 
def my_decorator(func):
    def wrapper():               #simple wrapper
        print("Before running")
        func()
        print("After running")
    return wrapper

#decorator around function
@my_decorator       
def say_hi():
    print("Helloo World")

say_hi()


#2 
def log_function_name(func):
    def wrapper():
        #printing the function name before executing 
        print(f"Calling function :  {func.__name__}" )   
        return func()
    return wrapper

@log_function_name
def greet():
    print("This is the function being executed.")

greet()


#3
def double_result(func):
    def wrapper(*args,**kwargs):
        res = func (*args, **kwargs)
        #takes result and returns the double of it 
        return res * 2
    return wrapper

@double_result
def res_doub(a,b):
    return a + b

print(res_doub(2,3))


#4
def log_arguments(func):
    def wrapper(*args,**kwargs):
        #decorator to print positional and keyword arguments
        print("Positional arguments : ", args)
        print("Keyword arguments : ", kwargs)
        return func(*args,**kwargs)
    return wrapper

@log_arguments
def fun(name, age=None):
    print(f"Hi {name}")

fun("Alice", age = 25)


#5
import time  #to measure execution time

#decorator to print how long a function tales to execute
def timer(func):
    def wrapper(*args,**kwargs):
        #time before the function runs
        start = time.time()
        result = func(*args,**kwargs)
        #time after the function finishes 
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result 
    return wrapper

@timer
def slow_function():
    time.sleep(1) #pausing for 1 sec

slow_function()


#6
def require_admin (func): 
    def wrapper(*args,**kwargs):
        #function to print when user=admin
        if kwargs.get("user") == "admin":
            return func(*args, **kwargs)
        #else to print access denied
        else :
            print("Access denied")
    return wrapper 

@require_admin 
def delete_database(user = None):
    #runs only if user=admin
    print("Database deleted!")

delete_database(user="guest") 
delete_database(user="admin")


#7
def repeat(n):
    def decorator(func):  #actual decorator
        def wrapper(*args,**kwargs):    #runs the function n times
            for _ in range(n):
                func(*args,**kwargs)
        return wrapper
    return decorator

@repeat(3)
#the decorator to let the function run this 3 times
def say_hi():
    print("Hi")

say_hi()

