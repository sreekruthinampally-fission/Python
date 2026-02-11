fruits = ["Orange", "Apple", "Mango"]
fruits.append("Banana")
print(fruits)

sec_fruits = ["Kiwi"]
fruits.extend(sec_fruits)
print(fruits)

fruits.insert(1,"Peach")
print(fruits)

fruits.remove("Peach")
print(fruits)

#fruits.pop(4)
fruits.pop()
print(fruits)

fruits.sort()
print(fruits)

print(fruits.count("Banana"))

fruits.reverse()
print(fruits)

sec_fruits = fruits.copy()
print(sec_fruits)

print(fruits.index("Apple"))

sec_fruits.clear()
print(sec_fruits)
