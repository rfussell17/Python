print("Program author: R. Fussell")
print("ID#: 3417846")
print("this program is using python 3")
print("Program 3 - Loops and if Conditions")
print("")


# this program prompts the user for a password, if not correct password, will prompt user again until correct
# then will prompt user for their name, if one of the 3 selected names, will craft a comment specific to them.
# if none of those names, it will produce a generic fallback comment saying "(their name), that's a nice name"

secret_password = "hello"
guess_count = 0
guess_limit = 10
while guess_count < guess_limit:
    guess = input("Password? ")
    guess_count = guess_count + 1
    if guess == secret_password:
        print("Welcome to the second half of the program!")
        break

name = input("What is your name? ")
if name == "Robin":
    print("What a great name!")
elif name == "Cher":
    print("Can i have your autograph, please?")
elif name == "Madonna":
    print("Can i have your autograph, please?")
else:
    print(name + ", that's a nice name")