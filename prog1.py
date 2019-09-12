print("Program author: R. Fussell")
print("ID#: 3417846")
print("this program is using python 3")
print("Program 1 - Math Functions")
print("")

# this program prompts the user for which math function they would like to use
# then accepts 2 input numbers to calculate with selected function (A, S, M, D, E, R)
# and finally displays the calculation on the screen
# if any other character is selected instead of A, S, M, D, E, R, an error message will print

# *****algorithm for program*****
# 1) display program name, author and information
# 2) display message "Please choose one of the following"
# 3) prompt user for math function input and display calculator options:
# (A)ddition, (S)ubtraction, (M)ultiplication,
# (D)ivision, (E)xponent, (R)emainder
# 4) store user input as math function choice
# 5) prompt user for first number
# 6) store first number as int_1
# 7) prompt user for second number
# 8) store second number as int_2
# 9) display calculation result of int_1 and int_2 with applied math function choice
# 10) if invalid character is chosen on step 3, error message will print


# let user know input is required
print("Please choose one of the following")
# empty print statement for spacing
print("")
# list choices for user, must pick one valid uppercase letter
choice = input("(A)ddition, (S)ubtraction, (M)ultiplication,"
               " (D)ivision, (E)xponent, (R)emainder: ")

# if user choice is A, display addition function
if choice.upper() == "A":
    # prompts user for first input number
    int_1 = input("Choose a number: ")
    # prompts user for second input number
    int_2 = input("Choose a second number: ")
    # prints the addition of input numbers on screen
    print(int(int_1) + int(int_2))

# if user choice is S, display subtraction function
elif choice.upper() == "S":
    # prompts user for first input number
    int_1 = input("Choose a number: ")
    # prompts user for second input number
    int_2 = input("Choose a second number: ")
    # prints the subtraction of input numbers on screen
    print(int(int_1) - int(int_2))

# if user choice is M, display multiplication function
elif choice.upper() == "M":
    # prompts user for first input number
    int_1 = input("Choose a number: ")
    # prompts user for second input number
    int_2 = input("Choose a second number: ")
    # prints the multiplication of input numbers on screen
    print(int(int_1) * int(int_2))

# if user choice is D, display division function
elif choice.upper() == "D":
    # prompts user for first input number
    int_1 = input("Choose a number: ")
    # prompts user for second input number
    int_2 = input("Choose a second number: ")
    # prints the division of input numbers on screen
    print(int(int_1) / int(int_2))

# if user choice is E, display exponent function
elif choice.upper() == "E":
    # prompts user for first input number
    int_1 = input("Choose a number: ")
    # prompts user for second input number
    int_2 = input("Choose a second number: ")
    # prints the exponent of input numbers on screen
    print(int(int_1) ** int(int_2))

# if user choice is R, display remainder function
elif choice.upper() == "R":
    # prompts user for first input number
    int_1 = input("Choose a number: ")
    # prompts user for second input number
    int_2 = input("Choose a second number: ")
    # prints the remainder of input numbers on screen
    print(int(int_1) % int(int_2))

# if A, S, M, D, E, R are not chosen, display error message
else:
    print("Error: Invalid Character Choice")
    print("Retry")
