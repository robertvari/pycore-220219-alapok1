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

with open("my_data.txt", "w") as my_textfile:
    my_textfile.write(str(phonebook))


# load file and print it's content
with open("my_data.txt") as my_textfile:
    print(my_textfile.read())
