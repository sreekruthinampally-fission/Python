#1 
for i in range(51):
    if i % 2 == 0:
        print(i)

#2
numb = [2,7,5,6]
max_numb = numb[0] 
for i in numb:
    if i > max_numb:
        max_numb = i
        print("Highest number is: ", i)

#3
for i in range(6):
    print("*" * i)

#4 
li = input("Enter elements separated by space: ").split()
print("List:", li)
mn = li[0]
for i in li:
    if i > mn:
        mn = i
        print("Highest Number is :", mn)

#5
n = 10
a = 0
b = 1
next = b  
count = 1
while count <= n:
    print(next, end=" ")
    count += 1
    a, b = b, next
    next = a + b

#6

