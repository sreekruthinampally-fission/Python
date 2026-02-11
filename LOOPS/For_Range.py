for letter in "Mount Everest":
    print(letter)

fruits = ["Apple","Orange","Mango","Peach" ]
for fruit in fruits:
    print(fruit)
    print(fruit,len(fruits))

users = {'Jim' : 'active', 'Stanley' : 'inactive', 'Dwight' : 'active', 'Toby' : 'active'}
active_users = {}
for user,status in users.items():
    if status == "active":
        active_users[user] = status
        print(active_users)

for i in range(5):
    print(i)

for j in range(3,11):
    print(j)

for k in range(0,10,3):
    print(k)

for l in range(-10,-100,-30):
    print(l)

colours = ["pink", "blue", "red", "purple", "violet"]
for col in range(len(colours)):
    print(col,colours[col])
    
names = ["Kav", "Rav", "Sav"]
for name in (names):
    print(name)
    if name == "Rav":
        print("Not a full name")

acro = ["Hi", "Hey", "Hello"]
for hola in range(len(acro)):
    print(hola)
    if hola == 1:
        print("Traditional")
    print(sum(range(hola)))

random = ["Yo", "Dude", "Bro"]
for rando in random:
    print(len(rando))
    print(len(random))

print(sum(range(7)))
