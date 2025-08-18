# Exercise

# Write an explicit infinite loop
# inside the infinite loop, read integer from user as an option

# If the option is 1: print here is your first step
# If the option is 2: print "you have some steps to go"
# If the option is 3: print "you are almost done"
# If the option is 4: quit from the loop

# If the option is other number: print it is an  invalid option

while True:
    option = input("Please enter an option (1-4): ")
    try:
        option = int(option)
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if option == 1:
        print("Here is your first step.")
    elif option == 2:
        print("You have some steps to go.")
    elif option == 3:
        print("You are almost done.")
    elif option == 4:
        print("Exiting the loop. Goodbye!")
        break
    else:
        print("It is an invalid option.")