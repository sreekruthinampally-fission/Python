import math
numb = [4,2,3,7]
max_res = numb[0]
for i in numb:
    if i > max_res:
        max_res == i
        print("Highest number is: ", i)

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
print()

for i in range(6):
    print("*" * i)
    
n = 11
if n <= 1:
    print(False)
else :
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n%i==0:
            is_prime = False
            break
    print(is_prime)

def rev(num):
    return int(num != 0) and ((num % 10) * \
            (10**int(math.log(num,10))) + \
                        rev(num // 10))

test_number = input("Enter a number: ")

res = test_number == rev(test_number)
print("Is the number palindrome? : " + str(res))

