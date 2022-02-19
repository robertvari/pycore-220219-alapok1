names = ["Csaba", "Robert", "Kriszta"]

# add items to list

print(names)
names.append("Tamás")
print(names)
names.append("Balázs")
print(names)

names.insert(0, "Andi")
print(names)

fruits = ["apple", "orange", "banan"]
#names = names + fruits
names += fruits

print(names)

# delete items from list
names.remove('apple')
print(names)

del names[0]
print(names)