friends = ["Jim","Toby","Mike"]
lucky_num = [9,0,7,2,3,4,5]
print(lucky_num)
print(friends[2])
print(friends[-2])

friends = ["Jim","Toby","Mike","Ellen","Chad"]
print(friends[0:])
print(friends[:])
print(friends[:4])
print(friends[1:4])

friends[2] = "Maya"
print(friends)

friends.extend(lucky_num)
print(friends)

friends.append("Lakshmi")
print(friends)

friends.insert(2,"Jolly")
print(friends)

friends.remove("Chad")
print(friends)

friends.clear()
print(friends)

friends = ["Jim","Toby","Mike","Mike","Ellen","Chad"]
friends.pop()
print(friends)

print(friends.index("Ellen"))
print(friends.count("Mike"))
frnds = friends.copy()
print(friends)
print(frnds[2])
print(frnds[-4])
print(frnds[2:4]) == ["Kelly", "Scott", "Dwight"]

