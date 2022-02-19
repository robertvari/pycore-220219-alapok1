name = input("What is your name?")
email = input("Email?")
phone = input("Phone?")
address = input("Address?")

phonebook = {}

phonebook[phone] = {
    "name": name,
    "address": address,
    "email": email
}

print(phonebook)