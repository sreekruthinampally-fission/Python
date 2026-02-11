f = lambda a : a*a
print(f(5))

x = lambda i,j : i + j
print(x(2,3))

def make_incrementor(n):
    return lambda y : y + n
 
#b = input("Enter the number that has to be incremented : ")
#d = input("Enter the value to increment it by : ")
#print(make_incrementor(b))

s1 = 'mount'
s2 = lambda func: func.upper()
print(s2(s1))

check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(4))  
print(check(7))

calc = lambda x , y : (x+y, x*y)
res = calc(3,4)
print(res)

