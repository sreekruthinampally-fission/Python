is_male = False
is_tall = True
if is_male and is_tall :
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are not a tall male")
elif not(is_male) and is_tall:
    print("You are not a male but tall")
elif not(is_male) and not (is_tall):
    print("You are neither a male nor tall")
elif is_male or is_tall:
    print("You are a male or you are tall or both")
else :
    print("Female")

def MaxNum(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    elif num1==num2==num3:
        return num1
    else:
        return num3
    
print(MaxNum(32,32,32))

if "dog" == "donkey":
    print("Fool")
else:
    print("not the same")

n1 = float(input("Enter your first number:"))
op = input("Enter your operator:")
n2 = float(input("Enter your second number:"))
if op == "+":
    print(n1+n2)
elif op == "-":
    print(n1 - n2)
elif op == "*":
    print(n1*n2)
elif op == "/":
    print(n1/n2)
else :
    print("Invalid Operator")
