text = input("Enter a text :")
num = int(input("Enter a number :"))
print(text * num)

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = (input("Enter any character : "))
print(str(a)*a + c + str(b)*b)

t1 = input("Enter first word : ")
t2 = input("Enter second word : ")
sep = input("Enter a separator : ")
print ( t1 , t2)
print (t1,t2, end = " ")
print(t1, sep, t2)
print(t1 + t2)

st = input("Enter a text : ")
numb = int(input("Enter a number : "))
ft = float(input("Enter a decimal number : "))
print(st)
print(numb + 10)
print(ft*10)

numb1 = int(input())
numb2 = int(input())
print(numb1 and numb2)
print(numb1 or numb2)
print(not numb1) 

a = 1
b = 2
c = 3
d = a ^ a
e = c ^ b
f = a & b
g = c | (a ^ a)
print(d)
print(e)
print(f)
print(g)

a = 4
b = 5
c = 6
d = a ^ a
e = c ^ b
f = a & b
g = c | (a ^ a)
print(d)
print(e)
print(f)
print(g)

d = float(input("Enter a number : "))
print("The integer value of", d , "is" , int(d))

num = input("Enter a number as a string : ")
num = int(num)
print(num * 2)

a = input("Enter a value : ")
b = input("Enter b value : ")
t = a
a = b 
b = t
print("After swapping : a -", a , " b -", b)

a = int(input("Enter a value : "))
n = int(input("Enter another value : "))
r = 2
nth_term = a * (r ** (n-1))
print(nth_term)

n = int(input("Enter a number : "))
print("Multiples of ", n, "are :")
for i in range(1,11):
    print(n * i, end =" ")

s = input("Enter a text : ")
for i in range(0,len(s),2):
    print(s[i])

x = int(input("Enter a number : "))
while x >= 0 :
    print(x, end=" ")
    x -= 1
    
x = int(input("Enter a number : "))
i = 1
while i * i <= x :
    print(i * i, end=" ")
    i += 1

x = int(input("Enter a number : "))
i = 1
while i <= x :
    print(i * i, end=" ")
    i += 1

n = int(input("Enter a number : "))
def neg(n):
    while n <= 0 :
        print(n)
        n += 1

def pos(n):
    while n >= 0:
        print(n)
        n -= 1
if n < 0:
    neg(n)
else :
    pos(n)

a = int(input("Enter a number : "))
if a > 100 :
    print("BIG")
else :
    print("small")

a = int(input("Enter a number : "))
if a % 3 == 0 and a % 5 == 0 :
    print("FIZZBUZZ!!")
elif a % 5 == 0:
    print("Buzz")
elif a % 3 == 0:
    print("Fizz")
else :
    print(a)

n = int(input("Enter a number : "))
if n % 2 == 0:
    print("friend")
else :
    print("You")

year = int(input("Enter a year : "))
if year % 4 == 0 and year % 100 != 0:
    print("LEAPP!!")
else :
    print("boo")

n1 = int(input("Enter a number : "))
n2 = int(input("Enter a smaller number than that : "))
for i in range(1,11):
    s1 = (n1 * i)
    s2 = (n2 * i)
    diff = s1 - s2
    print(diff, end = " ")
 
n = int(input("Enter a number : "))
for i in range(n):
    for j in range(n):
        print("* ", end=" " )
    print()

n = int(input("Enter a number : "))
i = 1
while i <= n :
    print("* " * i)
    i += 1

n = int(input("Enter a number : "))
for i in range(1, n + 1):
    for j in range(1, n + 2):
        if j == 1 or i == n or i == j:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
   
n = int(input("Enter a number : "))
while n >= 1:
    print("*" * n)
    n -= 1

n = int(input("Enter a number :"))
result = 1
for i in range(1,n + 1):
    result *= i
print(result)

n = int(input("Enter a number : "))
for i in range (1,n + 1):
    if n % i == 0:
        print(i, end =" ")

