import functools
import operator
from functools import reduce 

def add(x,y):
    return x + y

a = [1,2,3,4,5]
res = reduce(add, a)
print(res)

b = [1,2,3,4,5]
resn = reduce(lambda w,z : w*z, b)
print(resn)

r = [1,3,5,6,2]

print(functools.reduce(operator.add,a))
print(functools.reduce(operator.mul,a))
print(functools.reduce(operator.add,["yee", "yee", "skrr", "skrr"]))

c = [1,2,3]
dropdat = reduce(lambda d,e : d + e, c, 10)
print(dropdat)


