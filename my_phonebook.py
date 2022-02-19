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

# open("my_data.json", "w") creates a file object in memory
with open("my_data.json", "w") as my_file_object:
    json.dump(phonebook, my_file_object)


# load file and print it's content
with open("my_data.json") as my_file_object:
    my_phonebook = json.load(my_file_object)
    print(my_phonebook[phone])
