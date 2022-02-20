my_friends = ["robert", "csaba", "kriszta", "tamás", "balázs"]

for i in my_friends:
    print(i.upper())

# break
for n in my_friends:
    if n == "kriszta":
        break

    print(n)


# continue
for n in my_friends:
    if n == "kriszta":
        continue

    print(n)