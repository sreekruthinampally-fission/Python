def starts_a(w):
    return w.startswith("a")

def even(n):
    return n % 2 == 0

hyy = [1,2,3,4,5,6]
yu = list(filter(even, hyy))
print(yu)

ant = [7,8,9,10,11,12]
amr = list(filter(lambda f : f % 2 == 0, ant))
print(amr)

a = [13,14,15,16,17,18,19,20]
b = filter(lambda x : x % 2 == 0, a)
c = list(map(lambda x : x * 2, b))
print(c)

a = ["apple", "banana", "cherry", "kiwi", "grape"]
b = list(filter(lambda w : len(w) > 5, a))
print(b)

L = ["apple" , None, "", "Banana", 0, "cherry"]
A = list(filter(None, L))
print(A)

li = ["apple", "banana", "avocado", "cherry", "apricot"]
res = filter(starts_a, li)
print(list(res))