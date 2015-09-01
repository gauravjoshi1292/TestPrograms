# fileinput module has methods that let you replace text in a file,
# the alternative for this is to create a new file every time we want to replace some value in the file,
# write new data to this new file and then replace the original file with the new file
import fileinput


def register():
    """
    Function that displays the registration page
    :return: None
    """
    print("Registeration Page")

    while True:
        # Free is used to check if the username is taken. It is set to True initially which means username is free
        free = True
        # Prompt the user to enter hes name
        name = input("Enter username: ")

        # Open the file and read it line by line to see if the username is already present
        # If username is present in the file set free to False
        file = open("login_data.txt", "r")
        for line in file:
            n = line.split(": ")[0]
            # If username is already present in the file, ask the user if she wants to quit
            # If yes return otherwise keep going
            if name == n:
                print("User name already taken")
                key = input("Press 'q' to quit or any other key to enter a different username: ")
                if key == 'q':
                    return
                else:
                    free = False

        # If username is not present in the file we can go forward
        # Otherwise continue the loop and keep prompting user for a username which is free
        if free:
            break
        else:
            continue

        # Close the file
        file.close()

    # Open the file in append mode and append username and password separated by colon
    # For e.g. Jim: abc
    file = open("login_data.txt", "a")
    password = input("Enter password: ")
    file.write(name + ": " + password + "\n")
    file.close()
    print("Hurray! You have been registered, " + name + ".")
    do_operations(name)


def login():
    """
    Function that displays the login page
    :return: None
    """
    print("Login Page")

    # Prompt the user for username
    name = input("Enter user name: ")

    # Open the file in read mode
    file = open("login_data.txt", "r")

    # name_in_file is used to check if the name is present in the file. It is set to False initially but changes to True
    # if the name is found in the file
    name_in_file = False

    # Read the file line by line
    for line in file:
        # Get the name and password present on the current line
        nameAndPassword = line.split(": ")
        n = nameAndPassword[0]
        p = nameAndPassword[1].rstrip("\n")

        # If the entered name matches the name on the current line, we set name_in_file to True
        # Then we keep prompting user to enter a password, until it matches the one in the file
        if name == n:
            name_in_file = True
            while True:
                password = input("Enter password: ")
                # If the entered password matches the one in the file, user is logged in and is free to do operations
                if password == p:
                    print("Welcome back " + name + "! You are logged in!!")
                    do_operations(name)
                    break
                else:
                    # If the entered password doesn't match the one given in the file,
                    # Ask the user if she wants to quit, or she wishes to enter a new password
                    print("Invalid password")
                    key = input("If you don't remember password, press 'q' to quit. Press any other key to enter"
                                " password again: ")
                    if key == 'q':
                        return
                    else:
                        continue

    # If the entered user name was not found in the file, we ask user if she wants to quit or register
    if not name_in_file:
        print("Sorry, you are not registered. Please register first.")
        key = input("Press 'q' to quit. Press 'b' to go back to login page. Press any other key to register: ")
        if key == 'q':
            return
        elif key == 'b':
            login()
        else:
            register()


def newResults(userName):
    """
    Adds new results to the files based upon user's choice of sport
    :return: no return value
    """
    validInput = 0
    while validInput == 0:
        # See if the user has entered a valid input and if so use the corresponding file
        # If the value entered is invalid, prompt the user to enter a correct value
        sport = int(input("What sport do you want to input results for:\n1: Cycling\n2: Swimming\n3: Running\n"))
        if sport == 1:
            fileName = "cyclingstats.txt"
            validInput = 1
        elif sport == 2:
            fileName = "swimmingstats.txt"
            validInput = 1
        elif sport == 3:
            fileName = "runningstats.txt"
            validInput = 1
        else:
            print("Error please choose a valid number between 1 and 3\n")

        f = 0
        oldText = ""
        data = open(fileName, "r")
        for line in data:
            if userName in line:
                f = 1
                oldText = line.rstrip("\n")
        data.close()

        result = input("Enter the result: ")

        if f == 0:
            # Write the name and value separated by space into the file
            data = open(fileName, "a")
            data.write(userName + " ")
            data.write(result + "\n")
            data.close()
        else:
            # Add the new result to the results in the file separated by a space
            newText = oldText + " " + result
            for line in fileinput.input(fileName, inplace=True):
                newLine = line.replace(oldText, newText)
                print(newLine, end="")


def printBestEight(userName):
    """
    Prints best eight results from the files based upon user's choice of sport
    :return: no return value
    """
    validInput = 0
    while validInput == 0:
        # See if the user has entered a valid input and if so use the corresponding file
        # If the value entered is invalid, prompt the user to enter a correct value
        sport = int(input("Which sport do you want the best eight members for:\n1: Cycling\n2: Swimming\n3: Running\n"))
        if sport == 1:
            print("\nBest eight cyclists are:")
            fileName = "cyclingstats.txt"
            validInput = 1
        elif sport == 2:
            print("\nBest eight swimmers are:")
            fileName = "swimmingstats.txt"
            validInput = 1
        elif sport == 3:
            print("\nBest eight runners are:")
            fileName = "runningstats.txt"
            validInput = 1
        else:
            print("Error please choose a valid number between 1 and 3\n")

        bestEight = []  # list that will store the best eight results

        data = open(fileName, "r")

        # dictionary that contains name and values
        results = {}

        # read the file line by line
        for line in data:
            # split function splits a string if there are spaces between words
            # and returns a list of all the words in the string
            # the first element will be the name and the second will be the value
            name = line.split()[0]
            values = line.split()[1:]
            results[name] = [int(i) for i in values]
        data.close()

        n = 0
        # Now results dictionary contains all the results, we need best eight results from the dictionary
        while n < 8:
            min_val = 99999999999999
            name = ""
            best = 0
            n += 1
            index = 0

            # Find the minimum value in the dictionary
            for (key, values) in results.items():
                for i in range(len(values)):
                    if values[i] < min_val:
                        name = key
                        best = values[i]
                        min_val = values[i]
                        index = i
            # Print the minimum value and set it to a big number, so we don't get the same value next time
            print(name + ": ", end="")
            print(best)
            results[name][index] = 999999999999


def compareResults(userName):
    """
    Compares and prints the results for the two persons, the choice of sport is also given by the user
    :return: no return value
    """
    validInput = 0
    while validInput == 0:
        # See if the user has entered a valid input and if so use the corresponding file
        # If the value entered is invalid, prompt the user to enter a correct value
        sport = int(input("Which results do you want to compare\n1: Cycling\n2: Swimming\n3: Running\n"))
        if sport == 1:
            fileName = "cyclingstats.txt"
            validInput = 1
        elif sport == 2:
            fileName = "swimmingstats.txt"
            validInput = 1
        elif sport == 3:
            fileName = "runningstats.txt"
            validInput = 1
        else:
            print("Error please choose a valid number between 1 and 3\n")

    firstPerson = userName
    secondPerson = input("Enter the name of the second person: ")

    # these variables will contain the data corresponding to the persons entered by the user
    firstPersonData = ""
    secondPersonData = ""

    data = open(fileName, "r")
    for line in data:
        # get the values corresponding to both persons from the file
        name = line.split()[0]
        if name == firstPerson:
            value = line.split()[1:]
            firstPersonData = name + ": " + str(value)
        elif name == secondPerson:
            value = line.split()[1:]
            secondPersonData = name + ": " + str(value)
    data.close()

    print("\nHere's the result for comparison:")
    if firstPersonData:
        print(firstPersonData)
    else:
        print("No data found for " + firstPerson + ", enter your result first.")
    if secondPersonData:
        print(secondPersonData)
    else:
        print("No data found for " + secondPerson + ", please enter a name that is present in the file.")


def editResults(userName):
    """
    Updates the results for a particular person based upon user's input, choice of sport is also needed
    :return: no return value
    """
    validInput = 0
    while validInput == 0:
        # See if the user has entered a valid input and if so use the corresponding file
        # If the value entered is invalid, prompt the user to enter a correct value
        sport = int(input("Which results do you want to edit\n1: Cycling\n2: Swimming\n3: Running\n"))
        if sport == 1:
            fileName = "cyclingstats.txt"
            validInput = 1
        elif sport == 2:
            fileName = "swimmingstats.txt"
            validInput = 1
        elif sport == 3:
            fileName = "runningstats.txt"
            validInput = 1
        else:
            print("Error please choose a valid number between 1 and 3\n")

        oldText = ""
        inputName = userName
        oldValue = input("Enter the result you want to replace: ")

        data = open(fileName, "r")
        f = 0
        for line in data:
            name = line.split()[0]
            if name == inputName:
                # We found a name in the file that matches the input name given by the user, so we break
                # and we'll replace the value later on
                f = 1
                oldText = line.rstrip("\n")
                break
        data.close()

        newValue = input("Enter the new value: ")
        newText = ""

        # Replace the old value in the string with the new value
        oldTextList = oldText.split(" ")
        size = len(oldTextList)
        for i in range(size):
            if oldTextList[i] == oldValue:
                oldTextList[i] = newValue

        newText = " ".join(oldTextList)

        if f == 1:
            # We found a name in the file that matches user input,
            # So we'll replace the value now using the fileinput module
            for line in fileinput.input(fileName, inplace=True):
                newLine = line.replace(oldText, newText)
                print(newLine, end="")
        elif f == 0:
            # The input name was not found in the file so we don't do anything
            print("Can't edit the result. " + userName + " is not present in the file.")


def do_operations(userName):
    """
    Function that displays operations page
    :return: None
    """
    print("Welcome to operations page")

    mainMenu = ("What would you like to do?\n1: Enter new results \n2: Compare results \n3: Edit results \n4: Print best eight members \n"
                "Please choose a number ranging from 1 to 4 \n")

    validChoice = 0
    while validChoice == 0:
        # Ask the user for an operation
        choice = int(input(mainMenu))
        # See if the user has entered a valid input and if so use the corresponding file
        # If the value entered is invalid, prompt the user to enter a correct value
        if choice == 1:
            newResults(userName)
            validChoice = 1
        elif choice == 2:
            compareResults(userName)
            validChoice = 1
        elif choice == 3:
            editResults(userName)
            validChoice = 1
        elif choice == 4:
            printBestEight(userName)
            validChoice = 1
        else:
            validChoice = 0
            print("Error please choose a valid number between 1 and 4\n")

    go_back = input("Enter 'q' to quit or any other key to go back to operations menu: ")
    if go_back == 'q':
        return
    else:
        do_operations(userName)


def main():
    """
    Function that displays the main page for the club
    :return: None
    """
    print("Welcome to the Parkwood Vale Harriers club page")

    # Ask the person if she's an existing user
    # If yes take her to login page
    # If no take her to registration page
    # Also, after login or registration take her to operations page
    # If she presses 'q', quit

    while True:
        choice = input("Are you an existing user? Enter 'y or n' or press 'q' to quit: ")
        if choice == "q":
            break
        if choice == "y":
            login()
            break
        elif choice == "n":
            register()
            break
        else:
            print("Please enter a valid choice")

main()