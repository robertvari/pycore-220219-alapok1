# game constants
min_number = 1
max_number = 10
max_tries = 3

# random number
magic_number = 5

# show game intro
print("="*50, "MAGIC NUMBER", "="*50)

# f = formatted string
print(f"There is number between {min_number} and {max_number}. Can you guess it?")
print(f"You have {max_tries} tries.")

user_guess = input("Your guess:")

# game loop if wrong user_guess
while user_guess != str(magic_number):
    max_tries -= 1

    if max_tries == 0:
        print("You have no more tries :(")
        print("Maybe next time!")
        break

    print(f"Wrong number :( You have {max_tries} tries left.")
    user_guess = input("Your guess:")

# end game
if user_guess == str(magic_number):
    print(f"You win!!! My number was {magic_number}")
else:
    print("Game over...")