import json


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

# todo save data to file

with open("my_data.json", "w") as f:
    json.dump(phonebook, f)


# load file and print it's content
with open("my_data.json") as f:
    my_phonebook = json.load(f)
    print(my_phonebook[phone])
