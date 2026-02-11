#print multiplication table
num = int(input("Enter a number : "))
for i in range(1,11):
    print(num * i)

#print characters of string at even indices
s = input('Enter a string : ')
p = len(s) + 1
for i in range(0,p,2) :
    print(s[i])

#print numbers in decreasing order in single line
x = int(input('Enter a number x : '))
while x >= 0:
    print(x)
    x -= 1

#print squares of numbers till x
x = int(input('Enter a number : '))
s1=1
s=2
while(s1<=x):
    print(s1)
    s1=s**2
    s=s+1
    
#print numbers upto 0 for +ve and -ve
n = int(input("Enter a number : "))
def neg(n):
    while n <= 0 :
        print(n)
        n+=1
    
def pos(n):
    while n >= 0:
        print(n)
        n-=1    
if n < 0:
    neg(n)
elif n > 0:
    pos(n)
else :
    print("Already a zero")

#Big or Small
a = int(input("Enter a number : "))
if a > 100:
    print("Big")
else :
    print("Small")

#fizzbuzz
a = int(input("Enter a number : "))
if a % 3 == 0 and a % 5 == 0:
    print('FIZZBUZZ')
elif a % 3 == 0:
    print('FIZZ')
elif a % 5 == 0:
    print('BUZZ')
else :
    print(a)

#evenodd frnd you basket 
n = int(input("Enter a number : "))
if n % 2 == 0:
    print("Friend")
else :
    print("You")

#greatest of three
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))
if a >> b and a>> c :
    print(a)
elif b >> a and b >> c:
    print(b)
elif c>>b and c >> a:
    print(c)
elif a==b==c :
    print("equal")
else :
    print("ok")

#leap year
x = int(input("Enter a year : "))
if x % 400 == 0 :
    print("leap")
elif x % 4 == 0 and x % 100 != 0:
    print("leap")
else :
    print("no")

#calculator
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
opt = int(input("Enter a number : "))
if opt == 1:
    print(a+b)
elif opt == 2:
    print(a-b)
elif opt == 3:
    print(a*b)
else :
    print("Invalid Input")



