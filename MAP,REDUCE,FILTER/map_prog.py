s = ["1", "2", "3","4"]
res = map(int,s)
print(list(res))

def double(val):
    return val * 2

a= [1,2,3,4]
res = list(map(double,a))
print(res)

b = [2,4,6,8]
resnt = list(map(lambda x : x ** 2, b))
print(resnt)

def myfunc(a,b):
    return a + b
x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(x))

c = [1,2,3]
d = [4,5,6]
yee = list(map(lambda y,z : y + z, c,d))
print(yee)

fruits = ["apple", "banana", "cherry"]
yuh = list(map(str.upper,fruits))
print(yuh)

words = ["lemon", "citrus", "pulpy"]
skrr = list(map(lambda s: s[0], words))
print(skrr)

w = [' hello ', ' python ', ' world ']
holup = list(map(str.strip, w))
print(holup)

celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c : (c * 9/5) + 32, celsius))
print(fahrenheit)

a = [1,2,3]
b = [4,5,6]
res = list(map(lambda x,y : x+y, a,b))

