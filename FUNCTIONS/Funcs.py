def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        print("The maximum number is : ")
        return num1
    elif num2>=num1 and num2>=num3:
        print("The highest number is : ")
        return num2
    elif num3>=num1 and num3>=num2:
        print("The biggest number is : ")
        return num3
    else:
        print(num1 , num2, num3, "All are equal")

print("Give three numbers:")
a = input("First number : ")
b = input("Second number : ")
c = input("Third number : ")
res = max_num(a,b,c)
print(res)

def sum_of_list(n):
    res = 0
    for i in n:
        res += i
    return res
    
print("The sum is : ", sum_of_list((8,2,3,0,7)))

def multiply_all(x):
    prod = 1
    for li in x:
        prod = prod * li
    return prod

print("The product is :", multiply_all(((8,3,2,-1,7))))

def string_reverse(str1):
    rstr1 = ' '
    index = len(str1)
    while index > 0:
        rstr1 += str1[index - 1]
        index = index - 1
    return rstr1

print(string_reverse('1234abcd'))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a number to compute the factorial : "))
print(factorial(n))

def test_range(num):
    if num in range(11):
        print("%s is in the range" %str(num))
    else:
        print("No.")

test_range(6)

def coun_case(x):
    d = {"UPPER_CASE" : 0, "LOWER_CASE" : 0}
    for c in x :
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else :
            pass

    print("Original String : ", x)
    print("No. of upper case character : ", d["UPPER_CASE"])
    print("No. of lower case characters : ", d["LOWER_CASE"])

coun_case("Mount EveresT")
