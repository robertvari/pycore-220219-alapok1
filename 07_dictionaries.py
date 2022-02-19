phonebook = {
    #     key        value
    "06206473859": {"name": "Robert Vari", "address": "Budapest", "email": "mail.pythonsuli@gmail.com"},
    "06206473851": {"name": "Kiss Csaba", "address": "Debrecen", "email": "csaba@gmail.com"},
    "06309874653": {"name": "Kocsis Krisztina", "address": "Pécs", "email": "kriszta@gmail.com"}
}

print(phonebook["06206473859"]["email"])
print(phonebook["06206473859"]["name"])
print(phonebook["06206473859"]["address"])

del phonebook["06309874653"]["email"]
print(phonebook.keys())
print(phonebook.values())

# add item to dictionary
phonebook["1234"] = "Tamás"
print(phonebook)

phonebook["1234"] = {"name": "Kiss Tamás", "address": "Siófok", "email": "tamas@gmail.com"}
print(phonebook)