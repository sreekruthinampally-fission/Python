def validate_positive(func):
    def  wrapper(x,y):
        if x > 0 and y > 0:
            result = func(x,y)
            print("Result:", result)
        else :
            print("Invaalid input")
    return wrapper

@validate_positive
def multiply_numbers(x,y):
    return x * y

multiply_numbers(4,3)
multiply_numbers(-2,3)
multiply_numbers(0,6)