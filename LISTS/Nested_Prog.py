a = [2,3,4,5]
res = [x** 2 for x in a]
print(res)

list_comp = [0,1,2,3,4]
yuh = [val*2 for val in list_comp]
print(yuh)

new = [ i for i in range(10)]
print(new)

m = []
for i in range(5):
    m.append([])
    for j in range(5):
        m[i].append(j)

print(m)

m =[[c for c in range(5)] for r in range(5)]
print(m)

m = [[1,2,3], [4,5,6], [7,8,9]]
odds = []
for r in m:
    for e in r:
        if e % 2 != 0:
            odds.append(e)

print(odds)

m = [[1,2,3], [4,5,6],[7,8,9]]
odds = [e for r in m for e in r if e % 2 != 0]
print(odds)

m=[[1,2,3], [4,5], [6,7,8,9]]
flat = []
for s in m:
    for v in s:
        flat.append(v)

print(flat)

m=[[1,2,3], [4,5], [6,7,8,9]]
flat = [ v for s in m for v in s ]
print(flat)

m = [["apple", "banana", "cherry"],
     ["date", "fig", "grape"],
     ["kiwi", "lemon", "mango"]]
mod_m = []
for r in m:
    mod_r = []
    for f in r:
        mod_r.append(f.capitalize())
    mod_m.append(mod_r)

print(mod_m)

m = [["apple", "banana", "cherry"],
     ["date", "fig", "grape"],
     ["kiwi", "lemon", "mango"]]
mod_m = [[f.capitalize() for f in r] for r in m]
print(mod_m)
