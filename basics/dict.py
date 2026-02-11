

monthConv = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May"
}

print(monthConv["Jan"])
print(monthConv.get("Jan"))
print(monthConv.get("Luv"))
print(monthConv.get("Luv", "Not available"))



