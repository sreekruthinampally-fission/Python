def execution_logger(func):
    def wrapper(*args, **kwargs) :
        print(f"Starting execution of {func.__name__}")

        result = func(*args,**kwargs)

        print(f"Completed execution of {func.__name__}")
        return result 
    return wrapper

@execution_logger
def multiply_numbers(x, y):
    return x * y

output = multiply_numbers(5,3)
print("Result :", output)
