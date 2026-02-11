def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = fun(5)
for n in ctr:
    print(n)

def num():
    yield 1
    yield 2
    yield 3

for i in num():
    print(i)

sq = (x*x for x in range(1,6))
for val in sq:
    print(val)

def fun(m):
    for i in range(m):
        yield i

for n in fun(3):
    print(n,end=" ")

gen = (x*x for x in range(3))
print(list(gen))

